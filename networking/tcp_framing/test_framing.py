import socket
import struct
import unittest

from framing import ProtocolError, encode_message, recv_message, send_message


class FramingTests(unittest.TestCase):
    def setUp(self):
        self.left, self.right = socket.socketpair()
        self.addCleanup(self.left.close)
        self.addCleanup(self.right.close)
        self.left.settimeout(1)
        self.right.settimeout(1)

    def test_encode_length_big_endian(self):
        self.assertEqual(encode_message(b"hello"), struct.pack("!I", 5) + b"hello")

    def test_round_trip(self):
        send_message(self.left, b"networking")
        self.assertEqual(recv_message(self.right), b"networking")

    def test_empty_payload(self):
        send_message(self.left, b"")
        self.assertEqual(recv_message(self.right), b"")

    def test_fragmented_frame(self):
        self.left.sendall(struct.pack("!I", 3))
        for part in (b"a", b"b", b"c"):
            self.left.sendall(part)
        self.assertEqual(recv_message(self.right), b"abc")

    def test_frame_over_size_limit_rejected(self):
        self.left.sendall(struct.pack("!I", 99))
        with self.assertRaises(ProtocolError):
            recv_message(self.right, max_size=10)

    def test_incomplete_frame_rejected(self):
        self.left.sendall(struct.pack("!I", 5) + b"ab")
        self.left.shutdown(socket.SHUT_WR)
        with self.assertRaisesRegex(ProtocolError, "remaining"):
            recv_message(self.right)

    def test_non_bytes_rejected(self):
        with self.assertRaises(TypeError):
            encode_message("text")

    def test_sender_limit(self):
        with self.assertRaises(ProtocolError):
            encode_message(b"abc", max_size=2)


if __name__ == "__main__":
    unittest.main()
