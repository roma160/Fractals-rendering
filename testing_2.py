from vec import *
from tkinter import *
from PIL import Image, ImageTk
from numpy import *

a = array([
    [1, 2, 3, 4],
    [4, 2, 2, 1]
])

a = rot90(a)
print(max(a, key=float))