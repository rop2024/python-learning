def main():
    inp = input("Input operation: ")
    num1 = int(input("Enter first num: "))
    num2 = int(input("Enter second num: "))
    select(inp, num1, num2)


def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a // b

def select(char, a,b):
    if char == '+':
        print(f"Result:{add(a, b)}")
    elif char == '-':
        print(f"Result:{sub(a, b)}")
    elif char == '*':
        print(f"Result:{mul(a, b)}")
    elif char == "/":
        print(f"Result:{div(a, b)}")
    else:
        print("Invalid response")
        return

if __name__ == "__main__":
    main()