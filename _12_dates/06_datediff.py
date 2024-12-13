import datetime

def main():
    # date 1 input
    date1 = date_setter(10, 8, 2024)
    # date 2 input
    date2 = date_setter(20, 11, 2024)

    difference = abs(int(date1.day - date2.day))
    print(f"Difference between both days are {difference}")



def date_setter(date, month, year):
    return datetime.date(year, month, date)

if __name__ == "__main__":
    main()