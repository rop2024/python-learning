def main():
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))

        if x == 0 or y == 0:
            raise ZeroDivisionError("YOU can't divide a number by 0")

        a = 0

        if type(x) != type(a) or type(y) != type(a):
            raise ValueError("Type of values are not suitable for normal division calculation")

        if type(x) != type(y):
            raise TypeError("Type Mismatch error")

        result = x // y
        print(result)

    except ZeroDivisionError:
        print("You can't divide a number by 0")

    except TypeError:
        print("Both values should be of same time")

    except Exception as e:
        print(f"Some error occured !! -- {e}")

    finally:
        print("Closing the program")

if __name__ == "__main__":
    main()