number_set = []
while True:
    input_number = input("Enter a number: ")

    if int(input_number) != -1:
        number_set.append(int(input_number))
    else:
        break

max_number = 0
min_number = number_set[0]

for number in number_set:
    if number > max_number:
        max_number = number
print("The maximum number is " + str(max_number))

for number in number_set:
    if number < min_number:
        min_number = number
print("The minimum number is " + str(min_number))
