days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}
month = int(input("Enter the month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month number!")
else:
    # If February, ask if leap year
    if month == 2:
        leap_year = input("Is the year a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            days = 29
        else:
            days = 28
    else:
        days = days_in_month[month]
    print(f"Month {month} has {days} days.")
