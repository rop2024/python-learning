array = [1,0,0,2,7,3,4]
sorted = True
previous = array[0]

# for i in range(len(array)):
#     for j in range(len(array)):
#         if array[i] < array[j]:
#             sorted = True
#         else:
#             sorted = False

for i in range(len(array)):
    if previous < array[i]:
        sorted = True
    else:
        sorted = False
        break

    previous = array[i]

if sorted:
    print("Sorted array")
else:
    print("not sorted array")