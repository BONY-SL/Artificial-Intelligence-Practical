number = int(input("Enter Number : "))

for value in range(1, (number + 1)):
    if number % value == 0:
        print(value)
