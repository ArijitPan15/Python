# Computer Networks: TCP Message Framing

TCP is a **byte stream**, not a sequence of application messages. A single `recv()`
may return fewer bytes than the sender sent in one call. This module implements
a common framing protocol: a **four-byte big-endian unsigned length** followed
by the payload.

- `encode_message`: validate and serialize a single message
- `send_message`: use `sendall` so the whole frame is transmitted
- `recv_message`: read exactly the header and declared payload length
- `echo_server`: a simple local single-client example

Each message is limited to 1 MiB by default to avoid unbounded allocation.
The framing protocol is a teaching example, **not encrypted**; do not use it
for sensitive network traffic without TLS and additional application safeguards.

To start the server:

```bash
python framing.py
```

In a second Python process:

```python
import socket
from framing import send_message, recv_message

with socket.create_connection(("127.0.0.1", 9090)) as connection:
    send_message(connection, b"hello")
    print(recv_message(connection))
```

Run tests from this directory:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

`socket.socketpair` is used in the test suite; availability varies by platform.
