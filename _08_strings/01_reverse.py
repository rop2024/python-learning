string = input("Enter a string: ").lower()
temp = ""
size = len(string)

for i in range(size):
    temp += string[size - i - 1]


print(temp)