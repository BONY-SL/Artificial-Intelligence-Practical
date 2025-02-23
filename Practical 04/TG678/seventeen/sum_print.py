number_one = int(input("Enter number one : "))
number_two = int(input("Enter number two : "))


def add_number(n1, n2):
    sum_value = n1 + n2
    if 15 <= sum_value <= 20:
        return 20
    else:
        return sum_value


print(f"Answer is: {add_number(number_one, number_two)}")
