## Two numbers are entered through the keyboard.
## Write a program to find the value of one number
#  raised to the power of another.

def main():
    ## take input of base
    base = int(input("Enter value of base: "))

    ## take input of power
    power = int(input("Enter value of power: "))

    ## start a while loop, with counter var and power
    counter = 1
    value = 1
    while counter <= power:
        ## power var should be multiplied by itself
        value *= base
        ## till counter is equal to power
        counter += 1

    ## print value
    print(f"value : {value}")


main()