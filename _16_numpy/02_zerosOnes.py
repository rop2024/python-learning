import numpy as np

def main():
    a = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3],[2,3,4]])
    shape = a.shape

    print(a)
    print(f"Shape of a is {shape}")

    b = np.zeros((5,4), dtype= int)
    print(b)
    print(b.dtype)

    c = np.ones((1,3), dtype= int)

if __name__ == "__main__":
    main()