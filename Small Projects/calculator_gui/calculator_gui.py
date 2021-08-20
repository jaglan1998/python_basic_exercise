from tkinter import *


root = Tk()
root.title("Calculator")

e = Entry(root, width=60, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=2, pady=10)


def button_click(number):
    last_digit = e.get()
    e.delete(0, END)
    e.insert(0, str(last_digit) + str(number))


first_num, sign = 0, None  # initiate global variables


def button_math(op):
    global first_num
    first_num = float(e.get())  # gets whatever is on screen when choosing op
    e.delete(0, END)  # delete it
    global sign
    sign = op


def button_equal():
    sec_num = float(e.get())
    e.delete(0, END)
    if sign == '+':
        e.insert(0, first_num + sec_num)
    if sign == '-':
        e.insert(0, first_num - sec_num)
    if sign == '*':
        e.insert(0, first_num * sec_num)
    if sign == '/':
        e.insert(0, first_num / sec_num)
    return


def button_back():
    e.delete(len(e.get())-1)


def button_clear():
    e.delete(0, END)
    return


# define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_period = Button(root, text=".", padx=42, pady=20, command=lambda: button_click('.'))

button_clear = Button(root, text="Clear", padx=77, pady=15, command=button_clear)
button_back = Button(root, text="Backspace", padx=63, pady=15, command=button_back)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)

button_add = Button(root, text="+", padx=38, pady=20, command=lambda: button_math('+'))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_math('-'))
button_multiply = Button(root, text="x", padx=39, pady=20, command=lambda: button_math('*'))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_math('/'))

# position buttons on grid
button_period.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_equal.grid(row=6, column=2)
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_clear.grid(row=1, column=0, columnspan=2)
button_back.grid(row=1, column=2, columnspan=2)

button_add.grid(row=3, column=3)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=5, column=3)
button_divide.grid(row=6, column=3)


root.mainloop()

