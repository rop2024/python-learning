list = [1,1,1,2,2,2,3,3,3,3,4,4,5,5,5,5,5]
freq_list = {}

for i in list:
    if i in freq_list.keys():
        freq_list[i] += 1
    else:
        freq_list[i] = 1

print(freq_list)