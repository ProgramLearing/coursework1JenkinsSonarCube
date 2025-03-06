import sys

def decimal_to_hex(decimal_value):
    # Check if the input is a boolean
    if isinstance(decimal_value, bool):
        raise ValueError("Input cannot be a boolean.")

    # Handle string inputs that represent numbers (e.g., "1000")
    if isinstance(decimal_value, str):
        try:
            decimal_value = int(decimal_value)  # Try converting string to integer
        except ValueError:
            raise ValueError("Input must be a valid integer or a string that can be converted to an integer")

    # Check if the input is a float
    if isinstance(decimal_value, float):
        # Handle infinity and very large floats
        if decimal_value == float('inf') or decimal_value == float('-inf') or abs(decimal_value) > 1e308:
            raise ValueError("Input is too large and cannot be converted.")
        
        # Check if the float is essentially an integer or very close to one
        if abs(decimal_value - int(decimal_value)) < 1e-10:
            decimal_value = int(decimal_value)  # Convert to integer if very close
        elif not decimal_value.is_integer():  # Raise error if the float is not an integer or close to an integer
            raise ValueError("Input must be a non-negative integer or a float close to an integer")

    # Check if the input is an integer and not a negative number
    if not isinstance(decimal_value, (int, float)) or decimal_value < 0:
        raise ValueError("Input must be a non-negative integer")

    # If it's an integer, proceed with conversion
    if isinstance(decimal_value, int):
        hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        hexadecimal = ""
        num = decimal_value
        
        # Check if the number is zero
        if num == 0:
            return "0x0"  # Hexadecimal representation of zero
        
        # Process the conversion for other numbers
        while num != 0:
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16
        
        # Return the result with the '0x' prefix in lowercase
        result = f"0x{hexadecimal.lower()}"
        return result

    # For very large floating point values, handle as integers
    if isinstance(decimal_value, float) and decimal_value.is_integer():
        return hex(int(decimal_value))  # Convert to integer and get the hex

    return "0x0"  # Default case (should never be reached)

if __name__ == "__main__":
    print("\n")
    if len(sys.argv) > 1:
        try:
            decimal_value = sys.argv[1]  # Get the input as string (even if it's a number)
            decimal_value = float(decimal_value) if '.' in decimal_value else int(decimal_value)
            print(decimal_to_hex(decimal_value))
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Error: No input argument provided. Usage: python script.py <decimal_number>")
    print("\n")
