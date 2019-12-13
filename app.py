from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()

root.title("Zullu - Sliding Puzzle")
root.iconbitmap("./images/favicon.ico")
root.geometry("1250x650")

imgs = []
imgs_con = []

Label(root, text="Sliding Puzzle Game", font=("Helvetic", 29), fg="#0095ff").grid(
    row=0, column=0,  columnspan=5, sticky=W+E, pady=10)

state = []


def itemAlreadyExist(arr, item):
    if item in arr:
        return True
    arr.append(item)
    return False


def randomlyFill():
    global state
    rN = random.randint(0, 8)
    while (itemAlreadyExist(state, rN)):
        rN = random.randint(0, 8)


def changeState(initial, final):
    state[initial] = state[final]
    state[final] = 8


def move(row, column):
    if row == 1 and column == 0:
        if (state[1] == 8):
            changeState(1, 0)
            swap({"row": row, "column": column}, {"row": 1, "column": 1})
        elif (state[3] == 8):
            changeState(3, 0)
            swap({"row": row, "column": column}, {"row": 2, "column": 0})
    if row == 1 and column == 1:
        if (state[0] == 8):
            changeState(0, 1)
            swap({"row": row, "column": column}, {"row": 1, "column": 0})
        elif (state[2] == 8):
            changeState(2, 1)
            swap({"row": row, "column": column}, {"row": 1, "column": 2})
        elif (state[4] == 8):
            changeState(4, 1)
            swap({"row": row, "column": column}, {"row": 2, "column": 1})
    if row == 1 and column == 2:
        if (state[1] == 8):
            changeState(1, 2)
            swap({"row": row, "column": column}, {"row": 1, "column": 1})
        elif (state[5] == 8):
            changeState(5, 2)
            swap({"row": row, "column": column}, {"row": 2, "column": 2})
    if row == 2 and column == 0:
        if (state[0] == 8):
            changeState(0, 3)
            swap({"row": row, "column": column}, {"row": 1, "column": 0})
        elif (state[4] == 8):
            changeState(4, 3)
            swap({"row": row, "column": column}, {"row": 2, "column": 1})
        elif (state[6] == 8):
            changeState(6, 3)
            swap({"row": row, "column": column}, {"row": 3, "column": 0})
    if row == 2 and column == 1:
        if(state[5] == 8):
            changeState(5, 4)
            swap({"row": row, "column": column}, {"row": 2, "column": 2})
        elif (state[1] == 8):
            changeState(1, 4)
            swap({"row": row, "column": column}, {"row": 1, "column": 2})
        elif (state[3] == 8):
            changeState(3, 4)
            swap({"row": row, "column": column}, {"row": 2, "column": 0})
        elif (state[7] == 8):
            changeState(7, 4)
            swap({"row": row, "column": column}, {"row": 3, "column": 1})
    if row == 2 and column == 2:
        if (state[8] == 8):
            changeState(8, 5)
            swap({"row": row, "column": column}, {"row": 3, "column": 2})
        elif (state[4] == 8):
            changeState(4, 5)
            swap({"row": row, "column": column}, {"row": 2, "column": 1})
        elif (state[2] == 8):
            changeState(2, 5)
            swap({"row": row, "column": column}, {"row": 1, "column": 2})
    if row == 3 and column == 0:
        if (state[3] == 8):
            changeState(3, 6)
            swap({"row": row, "column": column}, {"row": 2, "column": 0})
        elif (state[7] == 8):
            changeState(7, 6)
            swap({"row": row, "column": column}, {"row": 3, "column": 1})
    if row == 3 and column == 1:
        if (state[8] == 8):
            changeState(8, 7)
            swap({"row": row, "column": column}, {"row": 3, "column": 2})
        elif (state[6] == 8):
            changeState(6, 7)
            swap({"row": row, "column": column}, {"row": 3, "column": 0})
        elif (state[4] == 8):
            changeState(4, 7)
            swap({"row": row, "column": column}, {"row": 2, "column": 1})
    if row == 3 and column == 2:
        if (state[5] == 8):
            changeState(5, 8)
            swap({"row": row, "column": column}, {"row": 2, "column": 2})
        elif (state[7] == 8):
            changeState(7, 8)
            swap({"row": row, "column": column}, {"row": 3, "column": 1})


def swap(intial, final):
    ir = intial['row']
    ic = intial['column']
    indexI = 3*(ir - 1) + ic
    fr = final['row']
    fc = final['column']
    indexF = 3*(fr - 1) + fc
    global imgs, imgs_con

    imgs[indexI] = ImageTk.PhotoImage(Image.open(
        './images/Layer ' + str(indexI) + '.jpg'))

    imgs[indexF] = ImageTk.PhotoImage(Image.open(
        './images/Layer 8.jpg'))

    imgs_con[indexI] = Button(root, image=imgs[indexI])
    imgs_con[indexF] = Button(root, image=imgs[indexF])

    imgs_con[indexI].grid(row=fr, column=fc)
    imgs_con[indexF].grid(row=ir, column=ic)


for x in range(9):
    randomlyFill()

for x in range(9):
    imgs.append(ImageTk.PhotoImage(Image.open(
        './images/Layer ' + str(state[x]) + '.jpg')))

img_con_0 = Button(root, image=imgs[0], command=lambda: move(1, 0))
imgs_con.append(img_con_0)
imgs_con[0].grid(row=1, column=0)

img_con_1 = Button(root, image=imgs[1], command=lambda: move(1, 1))
imgs_con.append(img_con_1)
imgs_con[1].grid(row=1, column=1)

img_con_2 = Button(root, image=imgs[2], command=lambda: move(1, 2))
imgs_con.append(img_con_2)
imgs_con[2].grid(row=1, column=2)

img_con_3 = Button(root, image=imgs[3], command=lambda: move(2, 0))
imgs_con.append(img_con_3)
imgs_con[3].grid(row=2, column=0)

img_con_4 = Button(root, image=imgs[4], command=lambda: move(2, 1))
imgs_con.append(img_con_4)
imgs_con[4].grid(row=2, column=1)

img_con_5 = Button(root, image=imgs[5], command=lambda: move(2, 2))
imgs_con.append(img_con_5)
imgs_con[5].grid(row=2, column=2)

img_con_6 = Button(root, image=imgs[6], command=lambda: move(3, 0))
imgs_con.append(img_con_6)
imgs_con[6].grid(row=3, column=0)

img_con_7 = Button(root, image=imgs[7], command=lambda: move(3, 1))
imgs_con.append(img_con_7)
imgs_con[7].grid(row=3, column=1)


img_con_8 = Button(root, image=imgs[8], command=lambda: move(3, 2))
imgs_con.append(img_con_8)
imgs_con[8].grid(row=3, column=2)

full_img = ImageTk.PhotoImage(Image.open('./images/full_pic.jpg'))
full_img_con = Label(root, image=full_img)
full_img_con.grid(row=1, column=3, columnspan=2, rowspan=3)


root.mainloop()
