from tkinter import *
from PIL import Image, ImageTk
from creating_image import *

root = Tk()
root.title("")
root.resizable(0, 0)

canvas = Canvas(root, width = 400, height = 400)
canvas.pack()

DE = DistanseEstimator(array((5, 0, 0)), cube_size=2)
test_image = getImage(255, 255, DE, (3, 2, 0), (0, 0))

img = ImageTk.PhotoImage(image=test_image)
canvas.create_image(0, 0, image=img, anchor="nw")

mainloop()