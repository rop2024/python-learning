import datetime

def main():
    input_date = int(input("Enter date: "))
    input_month = int(input("Enter: "))
    input_year = int(input("Enter year: "))

    date = datetime.date(input_year, input_month, input_date)

    print(f"{date.strftime('%A')}")


if __name__ == "__main__":
    main()