from main import create_token, verify_signature
import unittest


class TestChallenge4(unittest.TestCase):
    def setUp(self) -> None:
        self.token = (
            b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
            b".eyJsYW5ndWFnZSI6IlB5dGhvbi"
            b"J9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M"
        )

    def test_create_token(self):
        self.assertEqual(create_token({"language": "Python"}, "acelera"),
                         self.token)

    def test_type_error(self):
        self.assertRaises(TypeError, create_token(()))

    def test_verify_signature(self):
        self.assertEqual(verify_signature(self.token), {"language": "Python"})

    def test_invalid_signature_error(self):
        key = "aceleras"
        self.assertEqual(verify_signature(self.token, key), {"error": 2})

    def test_decode_error(self):
        token = (
            b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dG"
            b"hvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M42"
        )
        self.assertEqual(verify_signature(token), "Invalid crypto padding")
