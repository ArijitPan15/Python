"""Tests use a fake opener: no internet access or server required."""
import unittest
from urllib.error import HTTPError, URLError

from healthcheck import check_url


class FakeResponse:
    def __init__(self, status):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *details):
        return False


class HealthcheckTests(unittest.TestCase):
    def test_expected_response(self):
        result = check_url("https://example.com/health",
                           opener=lambda request, timeout: FakeResponse(204),
                           expected=204, clock=lambda: 10.0)
        self.assertTrue(result.healthy)
        self.assertEqual(result.status, 204)
        self.assertEqual(result.elapsed_ms, 0.0)

    def test_unexpected_response(self):
        result = check_url("https://example.com",
                           opener=lambda request, timeout: FakeResponse(201))
        self.assertFalse(result.healthy)
        self.assertEqual(result.status, 201)

    def test_http_error_retains_status(self):
        def fail(request, timeout):
            raise HTTPError(request.full_url, 503, "unavailable", {}, None)
        result = check_url("https://example.com", opener=fail)
        self.assertEqual(result.status, 503)
        self.assertFalse(result.healthy)

    def test_network_failure(self):
        def fail(request, timeout):
            raise URLError("connection refused")
        result = check_url("https://example.com", opener=fail)
        self.assertIsNone(result.status)
        self.assertIn("connection refused", result.error)

    def test_invalid_arguments(self):
        for url, timeout, expected in [
            ("ftp://example.com", 1, 200),
            ("https://example.com", 0, 200),
            ("https://example.com", 1, 700),
        ]:
            with self.subTest(url=url, timeout=timeout, expected=expected):
                with self.assertRaises(ValueError):
                    check_url(url, timeout=timeout, expected=expected)


if __name__ == "__main__":
    unittest.main()
