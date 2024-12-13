# input:
# scores = {
#     "Alice": [90, 92, 85],
#     "Bob": [78, 81, 79],
#     "Charlie": [95, 85, 100]
# }
# Expected Output:
# {"Alice": 89, "Bob": 79.33, "Charlie": 93.33}

def main():
    scores = {}
    result = {}
    students = []

    num = int(input("Enter number of students: "))
    for i in range(num):
        add(students)

    for items in students:
        scores[items["name"]] = items

    result = percent(scores)

    print(result)

def add(list):
    name = input("Enter name: ")
    marks = []
    for i in range(3):
        marks.append(int(input(f"Enter marks of sub {i+1}: ")))

    list.append({"name": name, "score":marks})
    print("---")


def percent(dict):
    result = {}
    for key, values in dict.items():
        result[key] = format((sum(values["score"]))/3, ".2f")

    return result


if __name__ == "__main__":
    main()