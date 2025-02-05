
def get_string(s):
    if len(s) < 2:
        return ""
    else:
        first_two_characters = s[:2]
        last_two_characters = s[-2:]

        return first_two_characters + last_two_characters


get_user_string = input("Please Enter Your String :")
result = get_string(get_user_string)
print(f"Resulting String : {result}")

