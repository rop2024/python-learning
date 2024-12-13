array = [1,0,0,2,7,3,4]
to_replace = len(array) - 1

for i in range(to_replace-1):
    if array[i] == 0:
#         swapping few things
          temp = array[i]
          array[i] = array[to_replace]
          array[to_replace] = temp
          to_replace -= 1

print(array)

