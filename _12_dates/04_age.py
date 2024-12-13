import datetime

def main():
    # input date, month and year of the birth
    input_date = int(input("Enter date of your birth : "))
    input_month = int(input("Enter month of your birth : "))
    input_year = int(input("Enter year of your birth : "))

    birthday = datetime.date(input_year, input_month, input_date)
    days = age_caculator(birthday)
    # pass it to function named age_calculator()
    print(days)

def age_caculator(date):
    days = (datetime.date.today() - date).days
    years = int(days)  // 365
    # month = (int(days) % 365) // 12
    return f"{days} days which is equal to {years} years and {None} months"

if __name__ == "__main__":
    main()