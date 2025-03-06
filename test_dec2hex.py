import sys
import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(decimal_to_hex(15), '0xf')
        self.assertEqual(decimal_to_hex(100), '0x64')
        self.assertEqual(decimal_to_hex(255), '0xff')

    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), '0x0')

    def test_large_numbers(self):
        self.assertEqual(decimal_to_hex(123456789), '0x75bcd15')
        self.assertEqual(decimal_to_hex(9999999999), '0x2540be3ff')
        self.assertEqual(decimal_to_hex(123456789123456789), hex(123456789123456789))
        self.assertEqual(decimal_to_hex(2**60), hex(2**60))
        self.assertEqual(decimal_to_hex(2**100), hex(2**100))
        self.assertEqual(decimal_to_hex(2**200), hex(2**200))
        self.assertEqual(decimal_to_hex(10**500), hex(10**500))

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)
        with self.assertRaises(ValueError):
            decimal_to_hex(-99999999)
        with self.assertRaises(ValueError):
            decimal_to_hex(-sys.maxsize - 1)
        with self.assertRaises(ValueError):
            decimal_to_hex("-0")
        with self.assertRaises(ValueError):
            decimal_to_hex(" -100")

    def test_float_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(10.5)
        with self.assertRaises(ValueError):
            decimal_to_hex(0.0001)
        with self.assertRaises(ValueError):
            decimal_to_hex(1.99999)
        with self.assertRaises(ValueError):
            decimal_to_hex(float("nan"))
        with self.assertRaises(ValueError):
            decimal_to_hex(float("inf"))
        with self.assertRaises(ValueError):
            decimal_to_hex(float("-inf"))
        with self.assertRaises(ValueError):
            decimal_to_hex(1e309)
        with self.assertRaises(ValueError):
            decimal_to_hex(-10.5)
        with self.assertRaises(ValueError):
            decimal_to_hex(-0.0001)
        with self.assertRaises(ValueError):
            decimal_to_hex(99.99999999999999)
        self.assertEqual(decimal_to_hex(1e20), hex(int(1e20)))
        self.assertEqual(decimal_to_hex(1e100), hex(int(1e100)))
        self.assertEqual(decimal_to_hex(1e308), hex(int(1e308)))
    
    def test_unreachable_case(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(None)
        with self.assertRaises(ValueError):
            decimal_to_hex([])
        with self.assertRaises(ValueError):
            decimal_to_hex({})
        with self.assertRaises(ValueError):
            decimal_to_hex(" 500 ")
    
    def test_float_integer_values(self):
        self.assertEqual(decimal_to_hex(100.0), '0x64')
        self.assertEqual(decimal_to_hex(2**50.0), '0x400000000000')

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("string")
        with self.assertRaises(ValueError):
            decimal_to_hex(True)
        with self.assertRaises(ValueError):
            decimal_to_hex(None)
        with self.assertRaises(ValueError):
            decimal_to_hex("1000abc")
        with self.assertRaises(ValueError):
            decimal_to_hex("")
        with self.assertRaises(ValueError):
            decimal_to_hex("数字")

    def test_hex_format(self):
        self.assertTrue(decimal_to_hex(255).startswith('0x'))
        self.assertTrue(decimal_to_hex(16).startswith('0x'))

    def test_power_of_two(self):
        self.assertEqual(decimal_to_hex(16), '0x10')
        self.assertEqual(decimal_to_hex(32), '0x20')
        self.assertEqual(decimal_to_hex(64), '0x40')
        self.assertEqual(decimal_to_hex(2**30), '0x40000000')
        self.assertEqual(decimal_to_hex(2**40), '0x10000000000')
        self.assertEqual(decimal_to_hex(2**50), '0x400000000000')
        self.assertEqual(decimal_to_hex(2**10), '0x400')
        self.assertEqual(decimal_to_hex(2**20), '0x100000')

    def test_command_line_argument(self):
        sys.argv = ["Dec2Hex.py", "100"]
        self.assertEqual(decimal_to_hex(int(sys.argv[1])), "0x64")
    
    def test_command_line_float_argument(self):
        sys.argv = ["Dec2Hex.py", "100.0"]
        self.assertEqual(decimal_to_hex(float(sys.argv[1])), "0x64")
    
    def test_command_line_invalid_input(self):
        sys.argv = ["Dec2Hex.py", "invalid"]
        with self.assertRaises(ValueError):
            decimal_to_hex(int(sys.argv[1]))
    
    def test_command_line_missing_argument(self):
        sys.argv = ["Dec2Hex.py"]
        with self.assertRaises(IndexError):
            decimal_to_hex(int(sys.argv[1]))
    
    def test_large_number_multiple_digits(self):
        self.assertEqual(decimal_to_hex(1234567890), '0x499602d2')
    
    def test_very_close_to_integer_with_precision(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(10.0000000000001)
    
if __name__ == "__main__":
    unittest.main()
