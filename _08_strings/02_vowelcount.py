string = input("Enter a string: ").lower()
count = 0

for i in string:
    if i in "aeiou":
        count += 1

print(f"Total number of vowels are {count}")