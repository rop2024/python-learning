array = [1,2,1]
reverse = array[::-1]
palindrome = False

for i in range(len(array)):
    if array[i] == reverse[i]:
        palindrome = True
    else:
        palindrome = False

if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")