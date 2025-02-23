# Function to check if all digits of a number are even
def all_digits_even(num: int) -> bool:
    return all(int(digit) % 2 == 0 for digit in str(num))


# Generate numbers in the range and filter them
even_digit_numbers = [str(num) for num in range(100, 401) if all_digits_even(num)]

# Print the result as a comma-separated sequence
print(",".join(even_digit_numbers))
