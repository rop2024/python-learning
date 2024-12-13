# Write a program which accept temperature in Farenheit and print it in centigrade.
# formula C=(F-32)/1.8

farenheit = float(input("Enter temperature(in Farenheit) :"))

celcius = (farenheit-32)/1.8

print(f"{farenheit} degree farenheit in celcius is {celcius}")

# we got the input, but the formating of celcius is not correct, we dont want this many decimals
# to solve this issue, we would use format()

print(f"{farenheit} degree farenheit in celcius is {format(celcius, ".2f")}")
# now we get much cleaner response