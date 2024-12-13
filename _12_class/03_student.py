class Student:
    total_student = 0
    male_count = 0
    female_count = 0

    def __init__(self, name, roll, gender):
        self.__name = name
        self.__roll = roll
        self.__marks = [0,0,0]
        self.__percent = 0
        self.__gender = gender

        Student.total_student += 1

        if self.__gender.lower() in ['m', 'male']:
            Student.male_count += 1
        else:
            Student.female_count +=1

    def percent(self):
        self.__percent = sum(self.__marks) // (len(self.__marks))
        return self.__percent


    def set_marks(self):
       for i in range(3):
           self.__marks[i] = int(input(f"Enter marks of subject {i+1}: "))
       print("-----")

       self.percent()
       return

    def __str__(self):
        return f"|{self.__name}|{self.__roll}|{self.__marks}|{self.__percent}|"


def main():
    students = []

    for i in range(3):
        name = input("Enter name : ")
        roll = i+1
        gender = input("Enter gender: ")
        student = Student(name, roll, gender)
        student.set_marks()
        percent = student.percent()
        students.append(student)
        print(f"{name} has {percent} percent")

    print("-----")
    print(f"Total number of students : {Student.total_student}")
    print(f"Male to female ratio: {Student.male_count} : {Student.female_count}")


if __name__ == "__main__":
    main()