from tkinter import *

def main():
    window()


def window():
    global root
    root = Tk()

    label = Label(root, text = "Enter ur name : ")

    enter = Entry(root, width = 50)

    button = Button(root, text = "click me !!", command = lambda : OnClick(enter))

    label.grid(row = 0, column= 0)
    enter.grid(row = 0, column= 1)
    button.grid(row = 0, column= 2)

        
    root.mainloop()


def OnClick(space):
    label = Label(root, text = space.get())
    label.grid(row = 1, column= 1)
    


if __name__ == "__main__":
    main()