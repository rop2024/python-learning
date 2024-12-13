array = [1,2,2,3,3,5,5,6,6]
temp = []

for i in array:
    if i not in temp:
        temp.append(i)

print(temp)
