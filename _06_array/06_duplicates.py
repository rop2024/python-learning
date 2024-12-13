array = [1,2,2,3,3,5,5,6,6]
temp = []

for i in array:
    if array.count(i) > 1:
        temp.append(i)

temp_2 = []
for i in temp:
    if i not in temp_2:
        temp_2.append(i)


print(f"List of duplicates values : {temp_2}")
