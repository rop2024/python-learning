from tkinter import *

def labels():
    root = Tk()

    # creating objects
    label1 = Label(root, text = "Hello ")
    label2 = Label(root, text = "World")
    label3 = Label(root, text = "Hello users")

    # loading objects
    label1.grid(row=0,column = 0)
    label2.grid(row=1,column = 1)
    label3.grid(row=0,column = 2)

    root.mainloop()

    # observe that the output is always centralized


def main():
    labels()


if __name__ == "__main__":
    main()