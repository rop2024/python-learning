def main():
    student = {} # key : name of student and value : information
    student_list = []
    count = int(input("Enter number of records: "))
    for i in range(count):
        add(student_list)

    # converting from lists to dict
    todict(student_list, student)


    for key, value in student.items():
        print(f"{key} {value["last_name"]} from {value["city"]}, {value["country"]} has age {value["age"]}")
        print(f"has skills like {value["skills"]}")

    # print(student)

    # getting length of dict
    print(len(student))

    #deleting records
    student.popitem()
    print(student)


def add(list):
    # append list
    first_name = input("Enter First name: ")
    last_name = input("Enter Second name: ")
    gender = input("Enter age(M/F): ").upper()
    age = int(input("Enter age: "))
    marital_status = bool(input("Marital Status(True/False): "))
    country = input("Enter country: ")
    city = input("Enter city: ")
    skills = input("Enter skills: ").split(" ")

    i = 1
    for skill in skills:
        skill.capitalize()

    print("----")

    list.append({"first_name":first_name, "last_name":last_name,"gender":gender,"age":age, "martial status": marital_status, "country":country,"city":city, "skills":skills})

def todict(list, dict):
    for item in list:
        dict[item["first_name"]] = item

if __name__ == "__main__":
    main()