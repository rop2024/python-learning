# School Management System:
# Build classes for Person, Student, Teacher, and Classroom.
# Student and Teacher should inherit from Person.
# The Classroom class should contain lists of Student and
# Teacher objects and methods to add or remove students and teachers.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person -  {self.name} and age is {self.age}"

class Student:
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student info - {super().__str__()} and his/her id is {self.student_id}"

class Teacher:
    def __init__(self):
        pass

class Classroom:
    def __init__(self):
        pass


def main():
    suresh = Person("Suresh", 20)
    print(suresh)

    prakash = Student("Prakash", 20, 1)
    print(prakash)

if __name__ == "__main__":
    main()