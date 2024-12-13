array = [1,2,7,3,4]
target = int(input("Enter target: "))
temp = []

for i in array:
    for j in array:
        if i + j == target:
            temp.append(i)
            temp.append(j)

print(temp)