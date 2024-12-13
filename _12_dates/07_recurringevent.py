import datetime

def main():
    input_date = int(input("Enter date : "))
    input_month = int(input("Enter month : "))

    date = recurring_event_year(input_date, input_month)
    print(date)

    date2 = recurring_event_month(input_date)
    print(date2)

def recurring_event_year(input_date, input_month):
    today = datetime.date.today()
    current_year = today.year
    next_event_date = datetime.date(current_year, input_month, input_date)

    if next_event_date <= today:
        next_event_date = datetime.date(current_year+1, input_month, input_date)

    return next_event_date

def recurring_event_month(input_date):
    today = datetime.date.today()
    # this would throw error in many circumstances, it would be better to use exception handling, play safe here
    next_event_date = datetime.date(today.year, today.month, input_date)

    if next_event_date <= today:
        next_event_date = datetime.date(today.year, today.month+1, input_date)

    return next_event_date

if __name__ == "__main__":
    main()


