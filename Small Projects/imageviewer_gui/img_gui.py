from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')  # main root window title
root.iconbitmap('img_gui.ico')  # adding icon

f1 = LabelFrame(root)  # making frame for the photo
f1.grid(row=0, column=0, columnspan=3)  # grid it with columnspan for 3 buttons

# getting all the images
img1 = ImageTk.PhotoImage(Image.open('img (1).jpg'))
img2 = ImageTk.PhotoImage(Image.open('img (1).jfif'))
img3 = ImageTk.PhotoImage(Image.open('img (2).jpg'))
img4 = ImageTk.PhotoImage(Image.open('img (3).jpg'))
img5 = ImageTk.PhotoImage(Image.open('img (3).jfif'))
img6 = ImageTk.PhotoImage(Image.open('img (2).jfif'))
imgList = [img1, img2, img3, img4, img5, img6]

# show first image
imgLabel = Label(f1, image=img1)
imgLabel.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

# status bar
imgStatus = Label(root, text=f'Image 1 of Image {len(imgList)} ', relief=SUNKEN, bd=1, anchor=E)
imgStatus.grid(row=2, column=0, columnspan=3, sticky=EW)


# button functions
def back_b(img_no):
    global b_exit, b_forward, b_back, imgLabel, imgStatus
    imgLabel.grid_forget()  # just to forget last grid to avoid overlapping
    imgLabel = Label(f1, image=imgList[img_no - 1])  # -1 to get the index of image
    imgLabel.grid(row=0, column=0, padx=20, pady=20, columnspan=3)
    # status bar change with the img no.
    imgStatus = Label(root, text=f'Image {img_no} of Image {len(imgList)} ', relief=SUNKEN, bd=1, anchor=E)
    imgStatus.grid(row=2, column=0, columnspan=3, sticky=EW)
    # if we press the >> button again, index will +1
    b_forward = Button(root, text='>>', padx=20, pady=20, command=lambda: forward_b(img_no + 1))
    # if we press teh << button
    b_back = Button(root, text='<<', padx=20, pady=20, command=lambda: back_b(img_no - 1))
    if img_no == 1:  # if we are on first image
        b_back = Button(root, text='<<', padx=20, pady=20, state=DISABLED)
    # grid buttons
    b_back.grid(row=1, column=0, padx=20, pady=20)
    b_forward.grid(row=1, column=2, padx=20, pady=20)
    return


def forward_b(img_no):
    global b_exit, b_forward, b_back, imgLabel, imgStatus
    imgLabel.grid_forget()  # just to forget last grid to avoid overlapping
    imgLabel = Label(f1, image=imgList[img_no - 1])  # -1 to get the index of image
    imgLabel.grid(row=0, column=0, padx=20, pady=20, columnspan=3)
    # status bar change with the img no.
    imgStatus = Label(root, text=f'Image {img_no} of Image {len(imgList)} ', relief=SUNKEN, bd=1, anchor=E)
    imgStatus.grid(row=2, column=0, columnspan=3, sticky=EW)
    # if we press the >> button again, index will +1
    b_forward = Button(root, text='>>', padx=20, pady=20, command=lambda: forward_b(img_no + 1))
    if img_no == len(imgList):  # if we are on last image
        b_forward = Button(root, text='>>', padx=20, pady=20, state=DISABLED)
    # if we press teh << button
    b_back = Button(root, text='<<', padx=20, pady=20, command=lambda: back_b(img_no - 1))
    # grid buttons
    b_back.grid(row=1, column=0, padx=20, pady=20)
    b_forward.grid(row=1, column=2, padx=20, pady=20)
    return


def exit_b():
    root.quit()
    return


# defining buttons
b_back = Button(root, text='<<', padx=20, pady=20, command=lambda: back_b(1), state=DISABLED)
b_exit = Button(root, text='Exit', padx=20, pady=20, command=exit_b)
b_forward = Button(root, text='>>', padx=20, pady=20, command=lambda: forward_b(2))
# griding buttons
b_back.grid(row=1, column=0, padx=20, pady=20)
b_exit.grid(row=1, column=1, padx=20, pady=20)
b_forward.grid(row=1, column=2, padx=20, pady=20)

root.mainloop()
