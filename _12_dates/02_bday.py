import datetime

date = int(input("Enter your birth date : "))
month = int(input("Enter your birth month : "))


birthdate = datetime.date(datetime.datetime.now().year, month, date)

if birthdate < datetime.date.today():
    birthdate = datetime.date(datetime.datetime.now().year + 1, month, date)

datebtwn = (birthdate - datetime.date.today()).days

print(f"Your next birthday is on : {birthdate}")
print(f"Thats {datebtwn} days from now")
