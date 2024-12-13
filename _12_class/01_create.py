class Student:
    count = 0
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        Student.count += 1

    def __str__(self):
        return f"{self.name} has roll of {self.roll}"

    def pos(self):
        print("Student")



# alice = Student("Alice", 1)
# bob = Student("Bob", 2)
# charlie = Student("Charlie", 3)

# print(f"{alice.name} with roll number {alice.roll}")
# print(f"{bob.name} with roll number {bob.roll}")
# print(f"{charlie.name} with roll number {charlie.roll}")


# trying loop
list = []
for i in range(3):
    name = input("Enter name: ")
    list.append(Student(name, i+1))

for i in range(3):
    print(list[i])

print(Student.count)

