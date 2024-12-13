string = input("Enter a string: ").lower()

reverse = string[::-1]

if string == reverse:
    print("True")
else:
    print("False")