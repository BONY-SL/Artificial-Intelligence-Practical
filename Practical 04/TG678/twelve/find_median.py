integer_list = []

while True:
    number = int(input("Enter Your Number To add The List : "))
    if number != -1:
        integer_list.append(number)
    else:
        break
print(integer_list)
integer_list.sort()
n = len(integer_list)
print(integer_list)
median_position = 0

if n % 2 != 0:
    median_position = (n + 1) / 2
    print("Median is :", integer_list[int(median_position-1)])
else:
    median_position = ((n/2)+((n/2)+1)) / 2
    median = (integer_list[int(median_position-1)] +
              ((median_position-(int(median_position))) *
               (integer_list[int(median_position)]-integer_list[int(median_position-1)])))
    print("Median is :", median)
