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
            decimal_to_hex(-1)  # Raises ValueError for negative inputs

    def test_large_number(self):
        # Test with a large positive number
        # A large number (123456789) should be correctly converted to hexadecimal
        self.assertEqual(decimal_to_hex(123456789), '0x75bcd15')  # Large number conversion

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
            decimal_to_hex("string")  # Should raise error for non-numeric types

    def test_boolean_input(self):
        # Test with a boolean input (should raise ValueError)
        # Boolean values should not be accepted as valid inputs
        with self.assertRaises(ValueError):
            decimal_to_hex(True)  # or decimal_to_hex(False)

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
        with self.assertRaises(ValueError):
            decimal_to_hex(1.99999)

    def test_very_large_positive(self):
        # Test with a very large positive number (e.g., 1e100)
        self.assertEqual(decimal_to_hex(int(1e100)), hex(int(1e100)))

    def test_large_negative_near_limit(self):
        # Test with a very large negative number near the system's maximum negative value
        with self.assertRaises(ValueError):
            decimal_to_hex(-sys.maxsize - 1)

    def test_power_of_two(self):
        # Test with numbers that are powers of two
        self.assertEqual(decimal_to_hex(16), '0x10')
        self.assertEqual(decimal_to_hex(32), '0x20')
        self.assertEqual(decimal_to_hex(64), '0x40')

    def test_sequence_of_numbers(self):
        # Test a sequence of numbers from 1 to 10
        expected_results = ['0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7', '0x8', '0x9', '0xa']
        for i in range(1, 11):
            self.assertEqual(decimal_to_hex(i), expected_results[i - 1])

    def test_hex_and_decimal_same(self):
        # Test numbers where hex representation and decimal are the same (e.g., 1)
        self.assertEqual(decimal_to_hex(1), '0x1')
        self.assertEqual(decimal_to_hex(16), '0x10')

    def test_smallest_input(self):
        # Test with the smallest valid input, zero
        self.assertEqual(decimal_to_hex(0), '0x0')

    def test_int_boundary_before_overflow(self):
        # Test with a large number just before integer overflow
        self.assertEqual(decimal_to_hex(sys.maxsize - 1), hex(sys.maxsize - 1))

    def test_negative_values(self):
        # Test with various negative numbers (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)
        with self.assertRaises(ValueError):
            decimal_to_hex(-2)
        with self.assertRaises(ValueError):
            decimal_to_hex(-3)

    def test_large_powers_of_two(self):
        # Test with large powers of two
        self.assertEqual(decimal_to_hex(2**10), '0x400')  # 2^10 = 1024 in decimal
        self.assertEqual(decimal_to_hex(2**20), '0x100000')  # 2^20 = 1048576 in decimal

    def test_small_negative_float(self):
        # Test with small negative float (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-0.0001)

    def test_large_float_values(self):
        # Test with very large floating point values (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(1e200)  # Very large float, exceeds max integer size

    def test_negative_float(self):
        # Test with negative float values (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-10.5)

    def test_very_close_to_integer(self):
        # Test with float values very close to an integer (should raise ValueError for 10.1)
        self.assertEqual(decimal_to_hex(10.0), '0xa')
        with self.assertRaises(ValueError):
            decimal_to_hex(10.1)

    def test_non_ascii_string(self):
        # Test with non-ASCII characters in string (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex("数字")  # Non-ASCII characters

    def test_max_integer_value(self):
        # Test with the maximum integer value (should convert correctly)
        self.assertEqual(decimal_to_hex(sys.maxsize), hex(sys.maxsize))

    def test_performance_with_large_input(self):
        # Test with an extremely large number for performance
        large_input = 10**100
        self.assertEqual(decimal_to_hex(large_input), hex(large_input))

    def test_numeric_string_input(self):
        # Test with a numeric string input (should be valid)
        self.assertEqual(decimal_to_hex("1000"), '0x3e8')  # string "1000" should be valid

    def test_large_sequence(self):
        # Test with a large sequence of numbers (1 to 1000)
        for i in range(1, 1001):
            self.assertEqual(decimal_to_hex(i), hex(i))

    def test_large_negative_powers_of_two(self):
        # Test with large negative powers of two (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-(2**10))

    def test_floating_point_powers_of_two(self):
        # Test with floating point representations of powers of two
        self.assertEqual(decimal_to_hex(1e3), hex(1000))

    def test_hex_decimal_conversion(self):
        # Test consistency between hex and decimal conversion
        for i in range(1, 100):
            decimal_value = i
            hex_value = decimal_to_hex(decimal_value)
            self.assertEqual(decimal_to_hex(int(hex_value, 16)), hex_value)

    def test_minimal_non_zero_input(self):
        # Test the minimal non-zero integer input (should be '0x1')
        self.assertEqual(decimal_to_hex(1), '0x1')

    def test_empty_input(self):
        # Test with empty input (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex("")
        
    #Test for Large Arbitrary-Precision Integers
    def test_large_arbitrary_precision_integer(self):
        large_number = 10 ** 200  # Very large number
        self.assertEqual(decimal_to_hex(large_number), hex(large_number))

    #Performance Stress Tests for Extremely Large Numbers
    def test_performance_with_extremely_large_input(self):
        large_input = 10**1000
        self.assertEqual(decimal_to_hex(large_input), hex(large_input))

    #Large Powers of Two
    def test_large_powers_of_two(self):
        self.assertEqual(decimal_to_hex(2**30), '0x40000000')
        self.assertEqual(decimal_to_hex(2**40), '0x10000000000')
        self.assertEqual(decimal_to_hex(2**50), '0x400000000000')

    #Multi-Digit Hexadecimal Numbers
    def test_large_number_multiple_digits(self):
        self.assertEqual(decimal_to_hex(1234567890), '0x499602d2')

    #Decimal to Hex and Back Conversion Consistency
    def test_decimal_to_hex_and_back(self):
        for i in range(1, 100):
            hex_value = decimal_to_hex(i)
            decimal_value = int(hex_value, 16)
            self.assertEqual(decimal_to_hex(decimal_value), hex_value)

    #Performance with Large Sequences (1-1000)
    def test_performance_with_large_sequence(self):
        for i in range(1, 1001):
            self.assertEqual(decimal_to_hex(i), hex(i))

    #Mix of Small and Large Numbers
    def test_mixed_large_and_small_numbers(self):
        self.assertEqual(decimal_to_hex(2), '0x2')
        self.assertEqual(decimal_to_hex(16), '0x10')
        self.assertEqual(decimal_to_hex(256), '0x100')
        self.assertEqual(decimal_to_hex(123456789123456789), '0x75bcd15')

    #Floating Point Representation as Integers
    def test_float_representations(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(1.0)  # Should raise ValueError as 1.0 is a float

    #Mixed Content Non-Numeric Strings
    def test_non_numeric_string_with_mixed_content(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("1000abc")  # Should raise ValueError

    #Very Close to Integer Values with More Precision
    def test_very_close_to_integer_with_precision(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(10.0000000000001)  # Should raise ValueError
	## Combined versions

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
            decimal_to_hex(-1)  # Raises ValueError for negative inputs

    def test_large_number(self):
        # Test with a large positive number
        # A large number (123456789) should be correctly converted to hexadecimal
        self.assertEqual(decimal_to_hex(123456789), '0x75bcd15')  # Large number conversion

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
            decimal_to_hex("string")  # Should raise error for non-numeric types

    def test_boolean_input(self):
        # Test with a boolean input (should raise ValueError)
        # Boolean values should not be accepted as valid inputs
        with self.assertRaises(ValueError):
            decimal_to_hex(True)  # or decimal_to_hex(False)

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
        with self.assertRaises(ValueError):
            decimal_to_hex(1.99999)

    def test_very_large_positive(self):
        # Test with a very large positive number (e.g., 1e100)
        self.assertEqual(decimal_to_hex(int(1e100)), hex(int(1e100)))

    def test_large_negative_near_limit(self):
        # Test with a very large negative number near the system's maximum negative value
        with self.assertRaises(ValueError):
            decimal_to_hex(-sys.maxsize - 1)

    def test_power_of_two(self):
        # Test with numbers that are powers of two
        self.assertEqual(decimal_to_hex(16), '0x10')
        self.assertEqual(decimal_to_hex(32), '0x20')
        self.assertEqual(decimal_to_hex(64), '0x40')

    def test_sequence_of_numbers(self):
        # Test a sequence of numbers from 1 to 10
        expected_results = ['0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7', '0x8', '0x9', '0xa']
        for i in range(1, 11):
            self.assertEqual(decimal_to_hex(i), expected_results[i - 1])

    def test_hex_and_decimal_same(self):
        # Test numbers where hex representation and decimal are the same (e.g., 1)
        self.assertEqual(decimal_to_hex(1), '0x1')
        self.assertEqual(decimal_to_hex(16), '0x10')

    def test_smallest_input(self):
        # Test with the smallest valid input, zero
        self.assertEqual(decimal_to_hex(0), '0x0')

    def test_int_boundary_before_overflow(self):
        # Test with a large number just before integer overflow
        self.assertEqual(decimal_to_hex(sys.maxsize - 1), hex(sys.maxsize - 1))

    def test_negative_values(self):
        # Test with various negative numbers (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)
        with self.assertRaises(ValueError):
            decimal_to_hex(-2)
        with self.assertRaises(ValueError):
            decimal_to_hex(-3)

    def test_large_powers_of_two(self):
        # Test with large powers of two
        self.assertEqual(decimal_to_hex(2**10), '0x400')  # 2^10 = 1024 in decimal
        self.assertEqual(decimal_to_hex(2**20), '0x100000')  # 2^20 = 1048576 in decimal

    def test_small_negative_float(self):
        # Test with small negative float (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-0.0001)

    def test_large_float_values(self):
        # Test with very large floating point values (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(1e200)  # Very large float, exceeds max integer size

    def test_negative_float(self):
        # Test with negative float values (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-10.5)

    def test_very_close_to_integer(self):
        # Test with float values very close to an integer (should raise ValueError for 10.1)
        self.assertEqual(decimal_to_hex(10.0), '0xa')
        with self.assertRaises(ValueError):
            decimal_to_hex(10.1)

    def test_non_ascii_string(self):
        # Test with non-ASCII characters in string (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex("数字")  # Non-ASCII characters

    def test_max_integer_value(self):
        # Test with the maximum integer value (should convert correctly)
        self.assertEqual(decimal_to_hex(sys.maxsize), hex(sys.maxsize))

    def test_performance_with_large_input(self):
        # Test with an extremely large number for performance
        large_input = 10**100
        self.assertEqual(decimal_to_hex(large_input), hex(large_input))

    def test_numeric_string_input(self):
        # Test with a numeric string input (should be valid)
        self.assertEqual(decimal_to_hex("1000"), '0x3e8')  # string "1000" should be valid

    def test_large_sequence(self):
        # Test with a large sequence of numbers (1 to 1000)
        for i in range(1, 1001):
            self.assertEqual(decimal_to_hex(i), hex(i))

    def test_large_negative_powers_of_two(self):
        # Test with large negative powers of two (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex(-(2**10))

    def test_floating_point_powers_of_two(self):
        # Test with floating point representations of powers of two
        self.assertEqual(decimal_to_hex(1e3), hex(1000))

    def test_hex_decimal_conversion(self):
        # Test consistency between hex and decimal conversion
        for i in range(1, 100):
            decimal_value = i
            hex_value = decimal_to_hex(decimal_value)
            self.assertEqual(decimal_to_hex(int(hex_value, 16)), hex_value)

    def test_minimal_non_zero_input(self):
        # Test the minimal non-zero integer input (should be '0x1')
        self.assertEqual(decimal_to_hex(1), '0x1')

    def test_empty_input(self):
        # Test with empty input (should raise ValueError)
        with self.assertRaises(ValueError):
            decimal_to_hex("")
        
    #Test for Large Arbitrary-Precision Integers
    def test_large_arbitrary_precision_integer(self):
        large_number = 10 ** 200  # Very large number
        self.assertEqual(decimal_to_hex(large_number), hex(large_number))

    #Performance Stress Tests for Extremely Large Numbers
    def test_performance_with_extremely_large_input(self):
        large_input = 10**1000
        self.assertEqual(decimal_to_hex(large_input), hex(large_input))

    #Large Powers of Two
    def test_large_powers_of_two(self):
        self.assertEqual(decimal_to_hex(2**30), '0x40000000')
        self.assertEqual(decimal_to_hex(2**40), '0x10000000000')
        self.assertEqual(decimal_to_hex(2**50), '0x400000000000')

    #Multi-Digit Hexadecimal Numbers
    def test_large_number_multiple_digits(self):
        self.assertEqual(decimal_to_hex(1234567890), '0x499602d2')

    #Decimal to Hex and Back Conversion Consistency
    def test_decimal_to_hex_and_back(self):
        for i in range(1, 100):
            hex_value = decimal_to_hex(i)
            decimal_value = int(hex_value, 16)
            self.assertEqual(decimal_to_hex(decimal_value), hex_value)

    #Performance with Large Sequences (1-1000)
    def test_performance_with_large_sequence(self):
        for i in range(1, 1001):
            self.assertEqual(decimal_to_hex(i), hex(i))

    #Mix of Small and Large Numbers
    def test_mixed_large_and_small_numbers(self):
        self.assertEqual(decimal_to_hex(2), '0x2')
        self.assertEqual(decimal_to_hex(16), '0x10')
        self.assertEqual(decimal_to_hex(256), '0x100')
        self.assertEqual(decimal_to_hex(123456789123456789), '0x75bcd15')

    #Floating Point Representation as Integers
    def test_float_representations(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(1.0)  # Should raise ValueError as 1.0 is a float

    #Mixed Content Non-Numeric Strings
    def test_non_numeric_string_with_mixed_content(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("1000abc")  # Should raise ValueError

    #Very Close to Integer Values with More Precision
    def test_very_close_to_integer_with_precision(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(10.0000000000001)  # Should raise ValueError
            
if __name__ == "__main__":
    unittest.main()
            
