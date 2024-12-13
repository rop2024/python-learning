string = input("Enter string : ").lower().split(" ")

longest = string[0]

for i in string:
    if len(longest) < len(i):
        longest = i

print(f"Longest element in string is : {longest}")