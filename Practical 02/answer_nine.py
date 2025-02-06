def integer_convert_to_binary(number):
    binary_digit_list = []
    while number != 0:
        binary_digit_list.append(str(number % 2))  # Convert to string to use join
        number = number // 2
    return ''.join(reversed(binary_digit_list))  # Join digits into one string

get_int = input("Enter an integer: ")
get_binary = integer_convert_to_binary(int(get_int))

print("Binary representation:", get_binary)
