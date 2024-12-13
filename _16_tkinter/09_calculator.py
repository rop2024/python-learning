from tkinter import *

def main():
    calculator()

def calculator():
    global root
    root = Tk()
    root.title("Calculator")
    # make a entry row
    global enter
    enter = Entry(root, width= 35, border= 5, borderwidth= 2)
    enter.grid(row = 0, column= 0, columnspan=3, rowspan= 2)

    # make buttons from 9 to 1 and 0 in the end
    b1 = Button(root,padx=40, pady= 20, text = "1", command = lambda: onClick('1'))
    b2 = Button(root,padx=40, pady= 20, text = "2", command = lambda: onClick('2'))
    b3 = Button(root,padx=40, pady= 20, text = "3", command = lambda: onClick('3'))

    b4 = Button(root,padx=40, pady= 20, text = "4", command = lambda: onClick('4'))
    b5 = Button(root,padx=40, pady= 20, text = "5", command = lambda: onClick('5'))
    b6 = Button(root,padx=40, pady= 20, text = "6", command = lambda: onClick('6'))

    b7 = Button(root,padx=40, pady= 20, text = "7", command = lambda: onClick('7'))
    b8 = Button(root,padx=40, pady= 20, text = "8", command = lambda: onClick('8'))
    b9 = Button(root,padx=40, pady= 20, text = "9", command = lambda: onClick('9'))
    
    b0 = Button(root,padx=40, pady= 20, text = "0", command = lambda: onClick('0'))

    # add buttons like + - clear and equals
    clear = Button(root,padx=30, pady= 20, text = "Clear", command = clr)
    bplus = Button(root,padx=39, pady= 20, text = "+", command= command_add)
    bminus = Button(root,padx=41, pady= 20, text = "-", command= command_minus)

    bequals = Button(root, padx = 40, pady = 20, text = "=", command= equals)

    # entering buttons in grid
    b9.grid(row = 2, column= 0)
    b8.grid(row = 2, column= 1)
    b7.grid(row = 2, column= 2)

    b6.grid(row = 3, column= 0)
    b5.grid(row = 3, column= 1)
    b4.grid(row = 3, column= 2)

    b3.grid(row = 4, column= 0)
    b2.grid(row = 4, column= 1)
    b1.grid(row = 4, column= 2)

    b0.grid(row = 5, column= 1)
    bplus.grid(row = 5, column= 0)
    bminus.grid(row = 5, column= 2)

    bequals.grid(row= 6, column = 2)

    clear.grid(row = 6, column= 1)
    

    root.mainloop()


def onClick(number):
    num = enter.get()
    enter.delete(0,END)
    enter.insert(0,num + number)
    

def clr():
    enter.delete(0,END)

def command_add():
    f_num = int(enter.get())
    enter.delete(0,END)

    global first_num
    first_num = f_num

    global op
    op = "AD"


def equals():
    s_num = int(enter.get())
    enter.delete(0,END)

    if op == "AD":
        enter.insert(0, int(first_num) + int(s_num))
    
    elif op == "MI":
        enter.insert(0, int(first_num) - int(s_num))


def command_minus():
    f_num = enter.get()
    enter.delete(0,END)

    global first_num
    first_num = f_num

    global op
    op = "MI"

if __name__ == "__main__":
    main()