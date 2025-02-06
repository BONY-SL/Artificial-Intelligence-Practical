def check_variable_type(var):
    if var.isdigit():
        return "The variable is an integer."
    elif isinstance(var, str):
        return "The variable is a string."
    else:
        return "The variable is neither an integer nor a string."

# Example usage
val = input("Enter a Input : ")

print(check_variable_type(val))
