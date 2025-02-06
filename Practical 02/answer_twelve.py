def check_variable_type(variable):
    if isinstance(variable, list):
        print("The variable is a list.")
    elif isinstance(variable, tuple):
        print("The variable is a tuple.")
    elif isinstance(variable, set):
        print("The variable is a set.")
    else:
        print("The variable is not a list, tuple, or set.")

# Get user input
user_input = input("Enter a variable (list, tuple, or set): ")


try:
    user_input = eval(user_input)
    check_variable_type(user_input)
except:
    print("Invalid input! Please enter a valid Python data structure.")
