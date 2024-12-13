import numpy as np

def main():
    array = np.arange(2,6)
    print(array)

    # creating a 3x3 matrix and filling it with values from 1 to 9
    array2 = np.arange(1,10).reshape(3,3)

    print(array2)

if __name__ == "__main__":
    main()