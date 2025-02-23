year = int(input("Enter year : "))
month = int(input("Enter Month [1-12] : "))
day = 0

fixedDayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, 13):
    if int(month) == i:
        day = int(input(f"Enter Day [1-{fixedDayList[i - 1]}]: "))
        getday = fixedDayList[i - 1]
        if day == getday and month == 12:
            day = 1
            month = 1
            year += 1
        elif day == getday:
            day = 1
            month += 1
        else:
            day += 1
        break

print("The next date is [yyyy-mm-dd] :", year, "-", month, "-", day)

# from datetime import date, timedelta
#
# # Get user input
# year = int(input("Input a year: "))
# month = int(input("Input a month [1-12]: "))
# day = int(input("Input a day [1-31]: "))
#
# try:
#     # Create a date object
#     current_date = date(year, month, day)
#
#     # Calculate the next day
#     next_date = current_date + timedelta(days=1)
#
#     # Print the next date in the expected format
#     print(f"The next date is [yyyy-mm-dd] {next_date.year}-{next_date.month}-{next_date.day}")
# except ValueError:
#     print("Invalid date input! Please enter a valid date.")

