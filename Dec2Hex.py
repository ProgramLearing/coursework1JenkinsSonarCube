import sys
import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):

    def test_positive_number(self):
        # Test with a positive number
        # 15 in decimal should be '0xf' in hex
        self.assertEqual(decimal_to_hex(15), '0xf')

    def test_zero(self):
        # Test with zero
        # 0 in decimal should be '0x0' in hex
        self.assertEqual(decimal_to_hex(0), '0x0')

    def test_negative_number(self):
        # Test with a negative number (should raise ValueError)
        # Negative inputs should raise an error
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)

    def test_large_number(self):
        # Test with a large positive number
        # A large number (123456789) should be correctly converted to hexadecimal
        self.assertEqual(decimal_to_hex(123456789), '0x75bcd15')

    def test_large_negative_number(self):
        # Test with a large negative number (should raise ValueError)
        # Large negative numbers are invalid inputs and should raise an error
        with self.assertRaises(ValueError):
            decimal_to_hex(-99999999)

    def test_boundary_value(self):
        # Test with boundary values (system max size for int)
        # sys.maxsize is typically the largest value the system can handle for an integer
        self.assertEqual(decimal_to_hex(sys.maxsize), hex(sys.maxsize))

    def test_float_input(self):
        # Test with a float input (should raise ValueError)
        # Floats are not valid inputs for this conversion, should raise ValueError
        with self.assertRaises(ValueError):
            decimal_to_hex(10.5)

    def test_non_integer_input(self):
        # Test with a non-integer input (should raise ValueError)
        # Non-integer inputs like strings should raise a ValueError
        with self.assertRaises(ValueError):
            decimal_to_hex("string")

    def test_boolean_input(self):
        # Test with a boolean input (should raise ValueError)
        # Boolean values should not be accepted as valid inputs
        with self.assertRaises(ValueError):
            decimal_to_hex(True)

    def test_large_positive_number(self):
        # Test with a very large number
        # A very large number (123456789123456789) should be converted to its correct hex representation
        self.assertEqual(decimal_to_hex(123456789123456789), hex(123456789123456789))

    def test_hex_format(self):
        # Test that the hexadecimal representation starts with '0x'
        # This test ensures that all returned hex values correctly start with the '0x' prefix
        hex_result = decimal_to_hex(255)  # 255 in decimal should be '0xff' in hex
        self.assertTrue(hex_result.startswith('0x'), f"Expected hex to start with '0x', got {hex_result}")

    def test_edge_case_small_positive(self):
        # Test with small positive numbers like 1 and 2
        # Ensure that small positive numbers are correctly converted
        self.assertEqual(decimal_to_hex(1), '0x1')
        self.assertEqual(decimal_to_hex(2), '0x2')

    def test_edge_case_large_positive(self):
        # Test with very large positive numbers
        # 9999999999 is a very large positive number and its correct hex conversion is tested here
        self.assertEqual(decimal_to_hex(9999999999), '0x2540be3ff')

    def test_edge_case_small_negative(self):
        # Test with small negative numbers (should raise ValueError)
        # Negative numbers like -2 should raise an error
        with self.assertRaises(ValueError):
            decimal_to_hex(-2)

    def test_edge_case_large_negative(self):
        # Test with very large negative numbers (should raise ValueError)
        # Large negative numbers should be rejected
        with self.assertRaises(ValueError):
            decimal_to_hex(-9999999999)

    def test_float_edge_case(self):
        # Test with a very small float value (should raise ValueError)
        # A small float like 0.0001 should raise an error
        with self.assertRaises(ValueError):
            decimal_to_hex(0.0001)

    def test_small_numbers(self):
        # Test small positive numbers like 10 and 100
        # 10 in decimal should be '0xa' in hex, 100 should be '0x64'
        self.assertEqual(decimal_to_hex(10), '0xa')
        self.assertEqual(decimal_to_hex(100), '0x64')

    def test_even_numbers(self):
        # Test even numbers like 8 and 16
        # 8 in decimal should be '0x8' and 16 should be '0x10'
        self.assertEqual(decimal_to_hex(8), '0x8')
        self.assertEqual(decimal_to_hex(16), '0x10')

    def test_odd_numbers(self):
        # Test odd numbers like 7 and 15
        # 7 in decimal should be '0x7' and 15 should be '0xf'
        self.assertEqual(decimal_to_hex(7), '0x7')
        self.assertEqual(decimal_to_hex(15), '0xf')

    def test_small_consecutive_numbers(self):
        # Test small consecutive numbers like 3 and 4
        # Ensure that small consecutive numbers are correctly converted to their hex equivalents
        self.assertEqual(decimal_to_hex(3), '0x3')
        self.assertEqual(decimal_to_hex(4), '0x4')

    def test_large_float(self):
        # Test with a very large float value (should raise ValueError)
        # Very large float values like 1e1000 should raise an error
        with self.assertRaises(ValueError):
            decimal_to_hex(1e1000)

    def test_empty_string(self):
        # Test with an empty string (should raise ValueError)
        # An empty string should raise an error, as it’s not a valid number
        with self.assertRaises(ValueError):
            decimal_to_hex("")

    def test_non_numeric_string(self):
        # Test with a non-numeric string (should raise ValueError)
        # Any string input that cannot be converted to an integer should raise a ValueError
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")

    def test_none_input(self):
        # Test with None as input (should raise ValueError)
        # None is not a valid input and should raise a ValueError
        with self.assertRaises(ValueError):
            decimal_to_hex(None)

    def test_smallest_positive(self):
        # Test with the smallest positive number (1)
        self.assertEqual(decimal_to_hex(1), '0x1')

    def test_smallest_even(self):
        # Test with the smallest even positive number (2)
        self.assertEqual(decimal_to_hex(2), '0x2')

    def test_smallest_odd(self):
        # Test with the smallest odd positive number (3)
        self.assertEqual(decimal_to_hex(3), '0x3')

    def test_very_large_negative(self):
        # Test with a very large negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-1e18)

    def test_float_very_close_to_integer(self):
        # Test with a float value that is very close to an integer (e.g., 1.99999)
        # This should raise a ValueError as it's still a float
        with self.assertRaises(ValueError):
            decimal_to_hex(1.99999)

    def test_very_large_positive(self):
        # Test with a very large positive number (e.g., 1e100)
        self.assertEqual(decimal_to_hex(int(1e100)), hex(int(1e100)))

    def test_large_negative_near_limit(self):
        # Test with a very large negative number near the system's maximum negative value
        # This should raise an error as it's outside the acceptable range for conversion
        with self.assertRaises(ValueError):
            decimal_to_hex(-sys.maxsize - 1)

    def test_power_of_two(self):
        # Test with numbers that are powers of two
        # Powers of two should be correctly represented in hexadecimal
        self.assertEqual(decimal_to_hex(16), '0x10')
        self.assertEqual(decimal_to_hex(32), '0x20')
        self.assertEqual(decimal_to_hex(64), '0x40')

    def test_sequence_of_numbers(self):
        # Test a sequence of numbers from 1 to 10
        expected_results = ['0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7', '0x8', '0x9', '0xa']
        for i in range(1, 11):
            self.assertEqual(decimal_to_hex(i), expected_results[i - 1])

    def t
