from tkinter import *

def function():
    global root

    root = Tk()

    label = Label(root, text = "Click on the button -- >")
    button = Button(root, text = "Click me",command=funx)

    label.grid(row = 0, column= 0)
    button.grid(row = 0, column = 1)

    root.mainloop()

def funx():
    label = Label(root, text = "you clicked the button")
    label.grid(row = 1, column = 0)
    

def main():
    function()

if __name__ == "__main__":
    main()

