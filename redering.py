from tkinter import *
from PIL import Image, ImageTk
from creating_image import *

root = Tk()
root.title("")
root.resizable(0, 0)

canvas = Canvas(root, width = 400, height = 400)
canvas.pack()

DE = DistanseEstimator(vec3((0, 0, 0)), ellipse_R=1)
#DE += DistanseEstimator(vec3((0, 2, 0)), ellipse_R=1)
test_image = getImage(255, 255, DE, vec3.create(-3, 1, 1), vec3.create(0, 0, 0))

img = ImageTk.PhotoImage(image=test_image)
canvas.create_image(0, 0, image=img, anchor="nw")

mainloop()