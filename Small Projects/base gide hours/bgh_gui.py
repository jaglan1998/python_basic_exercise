from tkinter import *
from bgh import *


root = Tk()
root.title("Guide Hours")
root.geometry("400x200")

l1 = Label(root, text='Sales:').grid(row=0, column=0, padx=10, pady=10, sticky=W)
l2 = Label(root, text='Late night sales:').grid(row=1, column=0, padx=10, pady=10, sticky=W)
e1 = Entry(root, justify=RIGHT, width=40)
e1.grid(row=0, column=1, padx=10, pady=10, sticky=E)
e2 = Entry(root, justify=RIGHT, width=40)
e2.grid(row=1, column=1, padx=10, pady=10, sticky=E)


def b_getresult():
    l1_sales = round(float(e1.get()), 2)
    l2_sales = round(float(e2.get()), 2)
    l3 = Label(root, text=f"BGH = {cal_bgh(l1_sales, l2_sales)}, LNH: {cal_lnh(l2_sales)}")
    l3.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    return


b = Button(root, text='Get Result', padx=5, pady=5, command=b_getresult)
b.grid(row=2, column=0, padx=10, pady=10, sticky=W)

root.mainloop()
