from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('img_gui.ico')

f1 = LabelFrame(root, padx=10, pady=10)
f2 = LabelFrame(root, padx=10, pady=10)
f1.pack(padx=10, pady=10)
f2.pack(padx=10, pady=10)


myImg1 = ImageTk.PhotoImage(Image.open('img (1).jpg'))
myImg2 = ImageTk.PhotoImage(Image.open('img (2).jpg'))
myImg3 = ImageTk.PhotoImage(Image.open('img (3).jpg'))
myImg4 = ImageTk.PhotoImage(Image.open('img (1).jfif'))
myImg5 = ImageTk.PhotoImage(Image.open('img (2).jfif'))
myImg6 = ImageTk.PhotoImage(Image.open('img (3).jfif'))

imgList = [myImg1, myImg2, myImg3, myImg4, myImg5, myImg6]
img_index = 0
myLabel = Label(f1, image=imgList[img_index])
myLabel.grid(row=0, column=0)


def button_back():
    global img_index, myLabel, button_back
    if img_index > 0:
        img_index -= 1
    # if img_index == 0:
    #     button_back = Button(f2, text="<<", padx=15, pady=10, command=button_back, state=DISABLED).grid(row=1, column=0)
    myLabel.grid_forget()
    myLabel = Label(f1, image=imgList[img_index])
    myLabel.grid(row=0, column=0)
    return


def button_forward():
    global img_index, myLabel, button_forward
    if img_index < len(imgList)-1:
        img_index += 1
    if img_index == len(imgList)-1:
        button_forward = Button(f2, text=">>", padx=15, pady=10, command=button_forward, state=DISABLED).grid(row=1, column=2)
    else:
        myLabel.grid_forget()
        myLabel = Label(f1, image=imgList[img_index])
        myLabel.grid(row=0, column=0)
    return

def button_exit():
    root.quit()


button_back = Button(f2, text="<<", padx=15, pady=10, command=button_back).grid(row=1, column=0)
button_forward = Button(f2, text=">>", padx=15, pady=10, command=button_forward).grid(row=1, column=2)
button_exit = Button(f2, text="Exit", padx=15, pady=10, command=button_exit).grid(row=1, column=1)

root.mainloop()
