## Write a program to print the following:

## make function for each pattern

def main():
    ## call all function here
    choice = int(input("Their are 5 patterns in this program, choose between 1 to 5 :"))

    ch_list = [1, 2, 3, 4, 5]
    if choice not in ch_list:
        print("Usage : (between 1 and 5)")
        return 1

    height = int(input("Enter height, should be below 8 :"))

    if height > 8:
        print("Usage : (Below 8)")
        return 2

    if choice == 1:
        pattern1(height)
    elif choice == 2:
        pattern2(height)
    elif choice == 3:
        pattern3(height)
    elif choice == 4:
        pattern4(height)
    elif choice == 5:
        pattern5(height)

    return 0


def pattern1(height):
    ## *
    ## **
    ## ***
    ## ****
    ## *****

    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print("*", end="")

        print()

    return 0


def pattern2(height):
    ##     *
    ##    **
    ##   ***
    ##  ****
    ## *****
    for i in range(1, height + 1):
        for k in range(1, height + 1 - i):
            print(" ", end="")

        for j in range(1, i + 1):
            print("*", end="")

        print()

    return 0


def pattern3(height):
    ##     *
    ##    ***
    ##   *****
    ##  *******
    ## *********
    for i in range(1, height + 1):
        for j in range(1, (height - i) + 1):
            print(" ", end="")

        for k in range(1, i):
            print("*", end="")

        print("*", end="")

        for l in range(1, i):
            print("*", end="")

        for m in range(1, (height - i) + 1):
            print(" ", end="")

        print()

    return 0


def pattern4(height):
    ##     1
    ##    222
    ##   33333
    ##  4444444
    ## 555555555

    for i in range(1, height + 1):
        for j in range(1, (height - i) + 1):
            print(" ", end="")

        for k in range(1, i):
            print(i, end="")

        print(i, end="")

        for l in range(1, i):
            print(i, end="")

        for m in range(1, (height - i) + 1):
            print(" ", end="")

        print()

    return 0


def pattern5(height):
    ##     1
    ##    212
    ##   32123
    ##  4321234
    ## 543212345

    for i in range(1, height + 1):
        for j in range(1, (height - i) + 1):
            print(" ", end="")

        for k in range(1, i):
            print(i - k + 1, end="")

        print(1, end="")

        for l in range(2, i + 1):
            print(l, end="")

        for m in range(1, (height - i) + 1):
            print(" ", end="")

        print()
    return 0


if __name__ == "__main__":
    main()