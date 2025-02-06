def decimal_to_hexadecimal(number):
    return hex(number)[2:].upper()  # Remove the '0x' prefix and convert to uppercase

# Example usage
get_int = int(input("Enter a decimal number: "))
hexadecimal = decimal_to_hexadecimal(get_int)
print(f"Hexadecimal representation: {hexadecimal}")
