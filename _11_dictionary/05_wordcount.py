string = input("Enter a line: ").lower().split(' ')
count = {}

for word in string:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

# print element with the highest freq
mode = max(count.values())
for key, value in count.items():
    if value == mode:
        print(f"Highest word : {key}")


