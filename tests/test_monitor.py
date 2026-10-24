
import unittest

from app.monitor import validate_url


class TestValidateUrl(unittest.TestCase):

    def test_valid_https_url(self):
        is_valid, error = validate_url(
            "https://httpbin.org/status/200"
        )

        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_reject_localhost(self):
        is_valid, error = validate_url(
            "http://localhost:5000"
        )

        self.assertFalse(is_valid)
        self.assertIn("Localhost", error)

    def test_reject_private_ip(self):
        is_valid, error = validate_url(
            "http://192.168.1.10"
        )

        self.assertFalse(is_valid)
        self.assertIn("Private", error)

    def test_reject_unsupported_scheme(self):
        is_valid, error = validate_url(
            "ftp://example.com"
        )

        self.assertFalse(is_valid)
        self.assertIn("HTTP and HTTPS", error)

    def test_reject_empty_url(self):
        is_valid, error = validate_url("")

        self.assertFalse(is_valid)
        self.assertIn("enter a url", error.lower())

    
    def test_reject_url_without_hostname(self):
        is_valid, error = validate_url("https:///posts/1")

        self.assertFalse(is_valid)
        self.assertIn("hostname", error.lower())

    def test_reject_url_with_credentials(self):
        is_valid, error = validate_url(
            "https://user:pass@example.com"
        )

        self.assertFalse(is_valid)
        self.assertIn("credentials", error.lower())

    def test_reject_loopback_ip(self):
        is_valid, error = validate_url("http://127.0.0.1")

        self.assertFalse(is_valid)
        self.assertIn("Private", error)



if __name__ == "__main__":
    unittest.main()
