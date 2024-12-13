# Write a program to calculate area of circle.
# formula for area of circle pie * (radius)square

# using math class, to calculate area of circle accurately

import math
radius = float(input("Enter radius : "))

area = format(math.pow(radius,2) * math.pi, ".3f")

print(f"area of circle : {area}")

