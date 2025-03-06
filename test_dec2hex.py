# test_dec2hex.py
import sys
import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):

    def test_positive_number(self):
        # Test with a positive number
        self.assertEqual(decimal_to_hex(15), '0xf')  # 15 in decimal is '0xf' in hex

    def test_zero(self):
        # Test with zero
        self.assertEqual(decimal_to_hex(0), '0x0')  # 0 in decimal is '0x0' in hex

    def test_negative_number(self):
        # Test with a negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)  # Raises ValueError for negative inputs

    def test_large_number(self):
        # Test with a large positive number
        self.assertEqual(decimal_to_hex(123456789), '0x75bcd15')  # Large number conversion

    def test_large_negative_number(self):
        # Test with a large negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-99999999)

    def test_boundary_value(self):
        # Test with boundary values (system max size for int)
        self.assertEqual(decimal_to_hex(sys.maxsize), hex(sys.maxsize))

    def test_float_input(self):
        # Test with a float input (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(10.5)  # Floats should be rejected

    def test_non_integer_input(self):
        # Test with a non-integer input (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex("string")  # Should raise error for non-numeric types

    def test_boolean_input(self):
        # Test with a boolean input (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(True)  # Boolean input should raise error

    def test_large_positive_number(self):
        # Test with a very large number
        self.assertEqual(decimal_to_hex(123456789123456789), hex(123456789123456789))

    def test_hex_format(self):
        # Test that the hexadecimal representation starts with '0x'
        hex_result = decimal_to_hex(255)  # 255 in decimal should be '0xff' in hex
        self.assertTrue(hex_result.startswith('0x'), f"Expected hex to start with '0x', got {hex_result}")

    def test_edge_case_small_positive(self):
        # Test with small positive numbers like 1 and 2
        self.assertEqual(decimal_to_hex(1), '0x1')
        self.assertEqual(decimal_to_hex(2), '0x2')

    def test_edge_case_large_positive(self):
        # Test with very large positive numbers
        self.assertEqual(decimal_to_hex(9999999999), '0x2540be3ff')  # This should be correct now

    def test_edge_case_small_negative(self):
        # Test with small negative numbers (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-2)
            
    def test_edge_case_large_negative(self):
        # Test with very large negative numbers (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-9999999999)

    def test_float_edge_case(self):
        # Test with a very small float value (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(0.0001)


if __name__ == "__main__":
    unittest.main()
