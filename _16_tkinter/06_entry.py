from tkinter import *

def main():
    window()

def window():
    root = Tk()

    label = Label(root, text = "Enter your name :")
    entr = Entry(root, width= 50)
    
    label.pack()
    entr.pack()

    root.mainloop()

if __name__ == "__main__":
    main()