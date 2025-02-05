user_input = input("Enter a string: ")

modified_string = ""

for index, char in enumerate(user_input):
    if index % 2 == 1:
        modified_string += char

print(modified_string)
