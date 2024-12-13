from tkinter import *

def main():
    windows()


def windows():
    global root
    root = Tk()

    intro = Label(root, text = "Choose one of the button :")
    b1 = Button(root, text = "1", command = OnClick)
    b2 = Button(root, text = "2", command = OnClick)
    b3 = Button(root, text = "3", command = OnClick)
    bquit = Button(root, text = "quit", command= root.quit)

    intro.grid(row=0, column=0, columnspan= 3)
    b1.grid(row = 1,padx=20, pady = 10, column= 0)
    b2.grid(row = 1,padx=20, pady = 10, column = 1)
    b3.grid(row = 1,padx=20, pady = 10, column= 2)

    bquit.grid(row = 2, column= 0,padx=20, pady = 10, columnspan= 3)

    root.mainloop()


def OnClick():
    print = Label(root, text = "You selected some number i dont want to tell")
    print.grid(row = 3, column = 0)

if __name__ == "__main__":
    main()