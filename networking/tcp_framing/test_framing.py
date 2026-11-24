import socket
import struct
import unittest

from framing import MAX_FRAME, receive_frame, send_frame


class FramingTests(unittest.TestCase):
    def setUp(self):
        self.sender, self.receiver = socket.socketpair()
        for sock in (self.sender, self.receiver):
            self.addCleanup(sock.close)
            sock.settimeout(1)

    def test_multiple_messages(self):
        for payload in (b"hello", b"", b"\x00\xff"):
            send_frame(self.sender, payload)
        for payload in (b"hello", b"", b"\x00\xff"):
            self.assertEqual(receive_frame(self.receiver), payload)

    def test_clean_eof(self):
        self.sender.shutdown(socket.SHUT_WR)
        self.assertIsNone(receive_frame(self.receiver))

    def test_partial_header(self):
        self.sender.sendall(b"\x00")
        self.sender.shutdown(socket.SHUT_WR)
        with self.assertRaises(EOFError):
            receive_frame(self.receiver)

    def test_partial_body(self):
        self.sender.sendall(struct.pack("!I", 5) + b"ab")
        self.sender.shutdown(socket.SHUT_WR)
        with self.assertRaises(EOFError):
            receive_frame(self.receiver)

    def test_oversized_header(self):
        self.sender.sendall(struct.pack("!I", MAX_FRAME + 1))
        with self.assertRaises(ValueError):
            receive_frame(self.receiver)

    def test_oversized_send(self):
        with self.assertRaises(ValueError):
            send_frame(self.sender, b"x" * (MAX_FRAME + 1))

    def test_fragmented_reads(self):
        class Fragmented:
            def __init__(self):
                self.data = bytearray(struct.pack("!I", 3) + b"abc")

            def recv(self, size):
                result = bytes(self.data[:min(size, 1)])
                del self.data[:len(result)]
                return result

        self.assertEqual(receive_frame(Fragmented()), b"abc")


if __name__ == "__main__":
    unittest.main()
