from tkinter import *

def funx():
    root = Tk()
    label = Label(root, text = "Click on this buttons -- ")
    button = Button(root, text = "Click me !!!")

    label.grid(row = 0, column= 0)
    button.grid(row = 0, column = 1)
    
    root.mainloop()
def main():
    funx()

if __name__ == "__main__":
    main()