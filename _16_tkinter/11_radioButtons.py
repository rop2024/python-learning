from tkinter import *

def main():
    root = Tk()
    root.title("Radio buttons")

    rb = Radiobutton(root, text="Button 1")

    rb.grid(row=0, column= 0)
    
    root.mainloop()

if __name__  == "__main__":
    main()