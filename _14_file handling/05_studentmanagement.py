# Student Data File Management
# make this again and next time add minor features then move on to better features

import csv, datetime, os

# run this block only once, when the file and fields has been created
fields = ["Roll no.", "Name", "Performance", "Dob", "Phone number"]
file = open("student.csv", "w")
cwriter = csv.writer(file)
cwriter.writerow(fields)

def main():
    try:
        student_manage()
    except Exception as e:
        print("-----")
        print("Some error occurred !!")
        print(f"Error - {e}")
        print("-----")

def student_manage():
    # student.csv file

    while True:
        x = choices()

        if x == 1:
            # add new records
            record = []
            file = open("student.csv", "a")
            cwiter = csv.writer(file)

            rollno = int(input("Enter roll number: "))
            name = input("Enter name: ")
            performance = input("Average performance of student[A,B,C,D,E,F]: ")
            date_birth = int(input("Date of brith(Just date) : "))
            month_birth = int(input("Month of birth(Just month) : "))
            year_birth = int(input("Year of birth(Just year): "))
            phone = input("Enter phone number: ")

            record = [rollno, name, performance,datetime.date(year_birth, month_birth,date_birth), phone]

            cwiter.writerow(record)
            file.close()
            print("RECORD ADDED SUCCESSFULLY !!")
            print("-----")


        elif x == 2:
            # find name and delete record
            target_name = input("Type the name of the record you want to delete: ").lower()

            file = open("student.csv", "r")
            creader = csv.reader(file)

            file2 = open("temp.csv", "w")
            cwriter = csv.writer(file2)

            header = next(creader)
            cwriter.writerow(header)

            for row in creader:
                search_name = row[1].lower()
                if target_name == search_name:
                    continue
                else:
                    cwriter.writerow(row)

            file.close()
            file2.close()

            os.remove("student.csv")
            os.rename("temp.csv", "student.csv")
            print("Record deleted successfully")
            print("-----")

        elif x == 3:
            # list all records
            file = open("student.csv", "r")
            cread = csv.reader(file)
            head = next(cread)

            rows = list(cread)

            
            print(rows)
            file.close()


        elif x == 0:
            break
        else:
            # wrong choice
            print("Wrong choice !! Try again")

def choices():
    print("-----")
    print("[0] Quit")
    print("[1] Add record")
    print("[2] Remove record")
    print("[3] List record")
    print("-----")

    return int(input("Enter choice :"))



if __name__ == "__main__":
    main()