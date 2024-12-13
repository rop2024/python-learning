## Write a program to enter the numbers till the
#  user wants and at the end it should display the maximum
#  and minimum number entered.

def main():
    ## use while loop, set condition = true
    max = min = int(input("Enter number:"))
    while True:
        ## initialize max and min var
        ## ask for input
        inp = int(input("Enter number: "))

        ## logic
        if inp > max:
            max = inp
        if inp < min:
            min = inp

        ## display result
        print(f"max input : {max}")
        print(f"min input : {min}")

        ## ask if user what to quit
        prompt = input("Do you want to quit(y/n): ").lower()

        if prompt == 'y':
            return 0
        else:
            continue


main()