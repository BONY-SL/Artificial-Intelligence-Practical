string_one = input("Enter a string 1: ")
string_two = input("Enter a string 2: ")

combined_string = string_one + ' ' + string_two
print("Original Combined String:", combined_string)

combined_list = list(combined_string)


space_index = combined_list.index(' ')

combined_list[space_index + 1], combined_list[0] = combined_list[0], combined_list[space_index + 1]

modified_combined_string = ''.join(combined_list)
print("Modified Combined String:", modified_combined_string)
