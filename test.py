from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Zullu The genius")
root.geometry("400x300")


def changeit():
    # global b1, img1
    img1 = ImageTk.PhotoImage(Image.open('./images/Layer 1.jpg'))
    b1 = Button(root, image=img1)
    b1.grid(row=0, column=0)


img1 = ImageTk.PhotoImage(Image.open('./images/Layer 0.jpg'))
b1 = Button(root, image=img1)
b1.grid(row=0, column=0)

b2 = Button(root, text="Click", command=changeit)
b2.grid(row=0, column=1)

root.mainloop()
