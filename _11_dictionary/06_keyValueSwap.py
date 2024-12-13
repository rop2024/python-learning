dict = {"1":5, "2":4, "3":2}
rev_dict = {}

for keys, values in dict.items():
    if values in rev_dict:
        rev_dict[values].append(keys)
    else:
        rev_dict[values] = keys

print(dict)
print(rev_dict)