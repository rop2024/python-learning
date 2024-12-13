array = [1,2,3,4,5]
size = len(array)
temp = []

for i in range(size):
    # temp[i] = array[size - i - 1]
    temp.append(array[size - i - 1])
print(temp)