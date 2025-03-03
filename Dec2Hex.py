import sys
#test1
def decimal_to_hex(decimal_value):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value
    print(f"Converting the Decimal Value {num} to Hex...")
    
    # Check incase the user enters 0 as the value
    if num == 0:
        return "0"
    
    # Process the conversion for other numbers
    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16
    
    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    #checks if the arguments provided are greater than 1 (the script needs 2 arguments (Dec2Hex.py + interger)
    if len(sys.argv) > 1:
        print("Arguments entered are greater than 1 so proceeding correctly")  # No input argument
        #if true attempt to convert the argument to an interger
        try:
            decimal_value = int(sys.argv[1])  # Try converting input to integer
            decimal_to_hex(decimal_value)
        #If a valid interger is not used then it is catched (when try doesn't work)
        except ValueError:
            print("Error: Please provide a valid integer. You have entered a non interger input")  # Catch non-integer input
    #if false then print out error message
    else:
        print("Error: No input argument provided. Usage: python script.py <decimal_number>")  # No input argument
