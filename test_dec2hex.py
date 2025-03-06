# test_dec2hex.py
import unittest
from Dec2Hex import dec_to_hex

class TestDec2Hex(unittest.TestCase):

    def test_positive_number(self):
        # Test with a positive number
        self.assertEqual(dec_to_hex(15), '0xf')  # 15 in decimal is '0xf' in hex

    def test_zero(self):
        # Test with zero
        self.assertEqual(dec_to_hex(0), '0x0')  # 0 in decimal is '0x0' in hex

    def test_negative_number(self):
        # Test with a negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            dec_to_hex(-1)  # Raises ValueError for negative inputs

    def test_large_number(self):
        # Test with a large positive number
        self.assertEqual(dec_to_hex(123456789), '0x75bcd15')  # Large number conversion

    def test_large_negative_number(self):
        # Test with a large negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            dec_to_hex(-99999999)

    def test_boundary_value(self):
        # Test with boundary values (system max size for int)
        self.assertEqual(dec_to_hex(sys.maxsize), hex(sys.maxsize))



if __name__ == "__main__":
    unittest.main()
