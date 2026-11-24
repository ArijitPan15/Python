"""Length-prefixed binary messages over blocking TCP sockets."""
import struct

HEADER = struct.Struct("!I")
MAX_FRAME = 1024 * 1024


def _read_exact(sock, size, *, allow_eof=False):
    data = bytearray()
    while len(data) < size:
        chunk = sock.recv(size - len(data))
        if not chunk:
            if allow_eof and not data:
                return None
            raise EOFError("connection closed inside frame")
        data.extend(chunk)
    return bytes(data)


def send_frame(sock, payload):
    """Send one bytes message; callers must serialize concurrent writers."""
    if not isinstance(payload, bytes):
        raise TypeError("payload must be bytes")
    if len(payload) > MAX_FRAME:
        raise ValueError("frame too large")
    sock.sendall(HEADER.pack(len(payload)) + payload)


def receive_frame(sock):
    """Return bytes, or None on clean EOF between frames."""
    header = _read_exact(sock, HEADER.size, allow_eof=True)
    if header is None:
        return None
    size, = HEADER.unpack(header)
    if size > MAX_FRAME:
        raise ValueError("frame too large")
    return _read_exact(sock, size)
