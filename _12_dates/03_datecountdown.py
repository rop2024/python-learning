import datetime


def main():
    event = input("Enter name of event: ")
    # take input from the user about the date, month and and confirm the year
    input_date = int(input("Enter date :"))
    input_month = int(input("Enter month : "))

    # 2 stages of confirmation, current or custom
    input_year = input("Do you want to use [current] year or [custom] year : ").lower()
    if input_year in ["current", "cur", "cu"]:
        input_year = datetime.date.today().year
    else:
        input_year = int(input("Enter custom year : "))
        if datetime.date(input_year, input_month, input_date) < datetime.date.today():
            print("Try again, quiting program")
            return

    # subtract both the date
    days = countdown(datetime.date(input_year, input_month, input_date))
    # return the date
    print(f"{event} would happen after {days} day(s)")




def countdown(date):
    # compare date and datetime.date.today() and returns in int how many days left
    return (date - datetime.date.today()).days


if __name__ == "__main__":
    main()