get_string = input("Enter Your Input :")

first_char = get_string[0]

replaced_string = first_char + get_string[1:].replace(first_char,'$')

print("Changed String:",replaced_string)