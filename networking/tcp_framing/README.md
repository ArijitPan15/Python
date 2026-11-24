# TCP message framing

TCP provides a byte stream, not message boundaries. This example uses a four-byte unsigned big-endian length followed by exactly that many payload bytes. Frames are limited to 1 MiB, including support for empty messages.

Python 3.9+; no dependencies.

Run from this directory:

    python -m unittest -v

Local demonstration (no external network required):

    import socket
    from framing import send_frame, receive_frame
    a, b = socket.socketpair()
    with a, b:
        a.settimeout(2)
        b.settimeout(2)
        send_frame(a, b"hello")
        print(receive_frame(b))

The same helpers work on connected blocking TCP sockets. Set timeouts before reading or writing. None indicates clean EOF; empty bytes indicate a valid empty message. EOFError means a truncated frame. Close the connection after malformed input, timeout, or partial write; the stream may no longer be synchronized. Serialize concurrent writers externally. This is a teaching protocol, not authentication, encryption, or a complete server.
