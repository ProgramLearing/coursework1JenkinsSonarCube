# test_dec2hex.py
import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):

    def test_positive_number(self):
        # Test with a positive number
        self.assertEqual(dec_to_hex(15), '0xf')

    def test_zero(self):
        # Test with zero
        self.assertEqual(dec_to_hex(0), '0x0')

    def test_negative_number(self):
        # Test with a negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            dec_to_hex(-1)

    def test_large_number(self):
        # Test with a large positive number
        self.assertEqual(dec_to_hex(123456789), '0x75bcd15')

if __name__ == "__main__":
    unittest.main()
