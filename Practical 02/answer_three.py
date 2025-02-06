number_one = input("Enter a number 1 : ")
number_two = input("Enter a number 2 : ")

number_product = int(number_one) * int(number_two)
number_sum = int(number_one) + int(number_two)


def return_answer():
    if number_product <= 1000:
        return number_product
    else:
        return number_sum



print("The answer is: " + str(return_answer()))

