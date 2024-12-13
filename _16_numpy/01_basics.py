import numpy as np

def main():
    # create an array
    a = np.array([1,2,3,4,5,6])
    print(a)

    print(a.ndim)

    b = np.array([[1,2,3,4],[5,6,7,8],[1,2,4,6]])
    size = b.shape
    print(f"B has these element {b} and size of {size}")
    print(b.dtype)
    


if __name__ == "__main__":
    main()
