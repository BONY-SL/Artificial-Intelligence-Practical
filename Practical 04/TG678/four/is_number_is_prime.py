number = int(input("Enter Your Number : "))

count = 0
divided_numbers = []

for value in range(1, (number + 1)):
    if number % value == 0:
        divided_numbers.append(value)
        count = count + 1

print("Number have Divided Values :", divided_numbers)

if count == 2:
    print(number, " is Prime Number")
else:
    print(number, " is not Prime Number")
