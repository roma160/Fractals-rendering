from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("")
root.resizable(0, 0)

canvas = Canvas(root, width = 400, height = 400)
canvas.pack()
test_image = Image.open("test_image.jpg")



img = ImageTk.PhotoImage(image=test_image)
canvas.create_image(0, 0, image=img, anchor="nw")

mainloop()