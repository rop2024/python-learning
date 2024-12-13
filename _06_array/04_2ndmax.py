array = [1,2,7,3,4]
max = max2 = array[0]

for i in array:
    if i > max:
        max2 = max
        max = i
    elif max2 < i < max:
        max2 = i

print(f"Max element is array is : {max}")
print(f"2nd Max element in array is : {max2}")