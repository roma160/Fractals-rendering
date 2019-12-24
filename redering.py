from tkinter import *
from PIL import Image, ImageTk
from creating_image import *

camera_pos = vec3.create(0, 0, 0)

root = Tk()
root.title("")
root.resizable(0, 0)

label = Label(root)
label.pack()


DE = DistanseEstimator(vec3.create(5, 0, 0), ellipse_R=1)

def upd_img(img) :
    test_img = ImageTk.PhotoImage(image=img)
    label.config(image=test_img)
    label.image = test_img

def get_img():
    global DE
    img = getImage(255, 255, DE, camera_pos, vec3.create(0, 0, 0))
    return img

def key(event):
    global camera_pos
    if repr(event.char) == "\'w\'":
        camera_pos += vec3.create(0, 0, 0.5)
    elif repr(event.char) == "\'s\'":
        camera_pos -= vec3.create(0, 0, 0.5)
    elif repr(event.char) == "\'a\'":
        camera_pos += vec3.create(0, 0.5, 0)
    elif repr(event.char) == "\'d\'":
        camera_pos -= vec3.create(0, 0.5, 0)
    elif repr(event.char) == "\'q\'":
        camera_pos += vec3.create(0.5, 0, 0)
    elif repr(event.char) == "\'e\'":
        camera_pos -= vec3.create(0.5, 0, 0)
    t = time.time()
    upd_img(get_img())
    print(time.time() - t)

upd_img(get_img())

root.bind_all("<Key>", key)

mainloop()