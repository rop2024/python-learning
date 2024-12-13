from tkinter import *

def basics():
    root = Tk()

    # things to send on display
    label = Label(root, text = "Hello World !!!")

    # pack it up and send it to root
    label.pack()

    # .mainloop() rendering is done through loops, so every frame is rendered continuously unless user specifies to stop
    root.mainloop()

def main():
    basics()

if __name__ == "__main__":
    main()