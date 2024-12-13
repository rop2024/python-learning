import numpy as np

def main():
    a = np.arange(1, 10).reshape(3,3)
    b = np.arange(10, 19).reshape(3,3)

    # adding 
    c = a + b

    # subtracting
    d = a - b

    # printing result for addition and subtraction
    print(c)
    print() # for a line break
    print(d)

    e = a * b

    f = a / b

    print(e)
    print()
    print(f)

    new = a.dot(b)
    print(new)


if __name__ == "__main__":
    main()