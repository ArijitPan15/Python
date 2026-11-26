"""Send and receive binary messages over TCP with a four-byte length prefix."""
from __future__ import annotations

import socket
import struct

HEADER_SIZE = 4
MAX_MESSAGE_BYTES = 1024 * 1024


class ProtocolError(ValueError):
    """Raised for invalid or truncated network frames."""


def _read_exact(connection: socket.socket, size: int) -> bytes:
    chunks: list[bytes] = []
    remaining = size
    while remaining:
        chunk = connection.recv(remaining)
        if not chunk:
            raise ProtocolError(f"Connection closed with {remaining} bytes remaining")
        chunks.append(chunk)
        remaining -= len(chunk)
    return b"".join(chunks)


def encode_message(message: bytes, max_size: int = MAX_MESSAGE_BYTES) -> bytes:
    """Return a big-endian uint32 length followed by the payload."""
    if not isinstance(message, bytes):
        raise TypeError("message must be bytes")
    if not 0 <= max_size <= 0xFFFFFFFF:
        raise ValueError("max_size must fit a uint32")
    if len(message) > max_size:
        raise ProtocolError("message exceeds configured maximum")
    return struct.pack("!I", len(message)) + message


def send_message(connection: socket.socket, message: bytes) -> None:
    """Send one framed message, including a possibly empty payload."""
    connection.sendall(encode_message(message))


def recv_message(connection: socket.socket, max_size: int = MAX_MESSAGE_BYTES) -> bytes:
    """Receive one complete frame, even when TCP fragments the payload."""
    if not 0 <= max_size <= 0xFFFFFFFF:
        raise ValueError("max_size must fit a uint32")
    size = struct.unpack("!I", _read_exact(connection, HEADER_SIZE))[0]
    if size > max_size:
        raise ProtocolError(f"Received frame size {size} exceeds maximum {max_size}")
    return _read_exact(connection, size)


def echo_server(host: str = "127.0.0.1", port: int = 9090) -> None:
    """Run a single-client echo server for local educational use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        print(f"Listening on {host}:{port}")
        client, address = server.accept()
        with client:
            print(f"Connected: {address}")
            try:
                while True:
                    send_message(client, recv_message(client))
            except ProtocolError:
                # A closed connection ends this small demo.
                pass


if __name__ == "__main__":
    echo_server()
