# Write a program which accept principle, rate and time from user and print the simple interest.

principle = float(input("Enter principle: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

interest = (principle * rate * time)/100

print(f"Interest is {interest}")
print(f"Final principle is {principle + interest}")
