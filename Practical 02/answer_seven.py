# Python program to iterate the first 10 numbers
# and print the sum of the current and previous number

previous_num = 0

print("Iterating through the first 10 numbers:")
for current_num in range(1, 11):
    total = current_num + previous_num
    print(f"Current Number: {current_num}, Previous Number: {previous_num}, Sum: {total}")
    previous_num = current_num
