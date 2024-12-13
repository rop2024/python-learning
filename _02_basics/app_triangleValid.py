# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered by the user. A triangle is valid if the sum of all the three angles is equal to 180
# degrees.

angle1 = int(input("Enter 1st angle: "))
angle2 = int(input("Enter 2nd angle: "))
angle3 = int(input("Enter 3rd angle: "))

if angle1 + angle2 + angle3 == 180:
    print(f"Its a valid triangle")
else:
    print(f"Not a valid triangle")

