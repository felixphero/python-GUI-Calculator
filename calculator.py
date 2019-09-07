from tkinter import *

root = Tk()
root.title("PCalc")


def click(args):
    if args == 1:
        number.set('1')
    elif args == 2:
        number.set('2')
    elif args == 3:
        number.set('3')
    elif args == 4:
        number.set('4')
    elif args == 5:
        number.set('5')
    elif args == 6:
        number.set('6')
    elif args == 7:
        number.set('7')
    elif args == 8:
        number.set('8')
    elif args == 9:
        number.set('9')
    elif args == 0:
        number.set('0')


number = StringVar()
display = Entry(root, text=number, bg="white", fg="green",
                font=("verdana", 10)).grid(columnspan="4")
button1 = Button(text="1", command=lambda: click(1)).grid(row="1", column="1")
button2 = Button(text="2", command=lambda: click(2)
                 ).grid(row="1", column="2")
button3 = Button(text="3", command=lambda: click(3)
                 ).grid(row="2", column="0")
button4 = Button(text="4", command=lambda: click(4)
                 ).grid(row="2", column="1")
button5 = Button(text="5", command=lambda: click(5)
                 ).grid(row="2", column="2")
button6 = Button(text="6", command=lambda: click(6)
                 ).grid(row="3", column="0")
button7 = Button(text="7", command=lambda: click(7)
                 ).grid(row="3", column="1")
button8 = Button(text="8", command=lambda: click(8)
                 ).grid(row="3", column="2")
button9 = Button(text="9", command=lambda: click(9)
                 ).grid(row="4", column="0")
button0 = Button(text="0", command=lambda: click(0)
                 ).grid(row="4", column="1")
buttonAdd = Button(text="+").grid(row="1", column="3")
buttonSub = Button(text="-").grid(row="2", column="3")
buttonMul = Button(text="x").grid(row="3", column="3")
buttonDiv = Button(text="÷").grid(row="4", column="2")
buttonEq = Button(text="=").grid(row="4", column="3")
buttonEq = Button(text=">").grid(row="1", column="0")


root.mainloop()
