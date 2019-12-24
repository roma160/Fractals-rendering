from vec import *
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("")

canvas = Canvas(root)
img1 = ImageTk.PhotoImage(image=Image.open("test_image.jpg"))
img2 = ImageTk.PhotoImage(image=Image.open("fig.png"))
canvas.create_image(0, 0, image = img1, anchor="nw")
canvas.pack()

def com():
    print("Click")
    canvas.create_image(0, 0, image=img2, anchor="nw")

button = Button(root, text="Hello", command=com)
button.pack()

root.mainloop()