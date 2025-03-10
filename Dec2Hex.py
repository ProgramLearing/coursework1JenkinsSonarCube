import sys
import math

def decimal_to_hex(decimal_value):
    if isinstance(decimal_value, bool):
        raise ValueError("Input cannot be a boolean.")
    if isinstance(decimal_value, str):
        try:
            decimal_value = int(decimal_value)
        except ValueError:
            raise ValueError("Input must be a valid integer or a string that can be converted to an integer")
    if isinstance(decimal_value, float):
        if math.isnan(decimal_value) or math.isinf(decimal_value) or abs(decimal_value) > 1e308:
            raise ValueError("Input is too large or invalid to be converted.")
        if abs(decimal_value - round(decimal_value)) < 1e-10:
            decimal_value = int(decimal_value)
        elif not decimal_value.is_integer():
            raise ValueError("Input must be a non-negative integer or a float close to an integer")
    if not isinstance(decimal_value, (int, float)) or decimal_value < 0:
        raise ValueError("Input must be a non-negative integer")
    if isinstance(decimal_value, int):
        hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        hexadecimal = ""
        num = decimal_value
        if num == 0:
            return "0x0"
        while num != 0:
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16
        return f"0x{hexadecimal.lower()}"
    if isinstance(decimal_value, float) and decimal_value.is_integer():
        return f"0x{int(decimal_value):x}"
    return "0x0"

def main():
    print("\n")
    if len(sys.argv) > 1:
        try:
            decimal_value = sys.argv[1]  
            decimal_value = float(decimal_value) if '.' in decimal_value else int(decimal_value)
            print(decimal_to_hex(decimal_value))
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Error: No input argument provided. Usage: python script.py <decimal_number>")
    print("\n")

if __name__ == "__main__":
    main()
