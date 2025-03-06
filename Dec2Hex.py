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
            raise ValueError("Input must be a non-negative integer")

    # Check if the input is a float very close to an integer (e.g., 10.0 should be accepted as 10)
    if isinstance(decimal_value, float):
        if abs(decimal_value - int(decimal_value)) < 1e-10:
            decimal_value = int(decimal_value)  # Convert to integer if close to integer
        elif abs(decimal_value) > 1e308:  # Float overflow handling (e.g., 1e1000)
            raise ValueError("Input is too large and cannot be converted.")
        else:
            raise ValueError("Input must be a non-negative integer")

    # Check if the input is an integer and not a negative number
    if not isinstance(decimal_value, int) or decimal_value < 0:
        raise ValueError("Input must be a non-negative integer")

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value
    
    print(f"Converting the Decimal Value {num} to Hex..." + "\n")

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
    
    print(f"Hexadecimal representation is: {result}")
    return result  # Return the hexadecimal value for testing

if __name__ == "__main__":
    print("\n")
    if len(sys.argv) > 1:
        print("Arguments entered are greater than 1 so proceeding correctly")
        try:
            decimal_value = sys.argv[1]  # Get the input as string (even if it's a number)
            decimal_to_hex(decimal_value)
        except ValueError:
            print("Error: Please provide a valid integer. You have entered a non-integer input")
    else:
        print("Error: No input argument provided. Usage: python script.py <decimal_number>")
    print("\n")
