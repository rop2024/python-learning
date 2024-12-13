# Write a program to determine whether the year is a leap year or not. Any year is input by the
# user.

year = int(input("Enter year: "))

if year % 4 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
