from PIL import Image
from numpy import array, sqrt, radians
import numpy as np
from decimal import Decimal

zero = 0.0001
camera_view_angle = 100
max_iters = 2

class Light:
    position = (0, 0, 0)
    strength = 0

    def __init__(self, position, strength):
        self.position = position
        self.strength = strength

    #def calculate_ray(self, position):


class MergeTraysing :
    camera_pos = (0, 0, 0)
    camera_size = (0, 0)
    camera_rotation = (0, 0)

    def __init__(self, camera_position, camera_size, camera_rotation, DE):
        self.camera_pos = camera_position
        self.camera_size = camera_size
        self.camera_rotation = camera_rotation
        self.DE = DE
        #self.lights = light

    def ray(self, position, last_pos, iter) :
        min_dist = self.DE.DE(position)
        vect = position - last_pos
        last_pos = position.copy()
        position += vect * min_dist / vect.max()
        if self.DE.DE(position) <= zero :
            return 1 - self.DE.DE(position)/self.DE.DE(last_pos)
        elif iter > max_iters :
            return 0
        else :
            return self.ray(position, last_pos, iter + 1)

    def start_ray(self, x, y) :
        min_delta = self.DE.DE(array(self.camera_pos))
        z_angle = radians(self.camera_rotation[0]) + np.arctan(
            2*(self.camera_size[0]/2 - x)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size[0]
            )
        pos_x = self.camera_pos[0] + np.cos(z_angle)*min_delta
        pos_y = self.camera_pos[1] + np.sin(z_angle)*min_delta

        y_angle = radians(self.camera_rotation[1]) + np.arctan(
            2*(self.camera_size[1]/2 - y)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size[1]
            )
        pos_z = self.camera_pos[2] + np.sin(y_angle)*min_delta
        return self.ray(array([pos_x, pos_y, pos_z]), array(self.camera_pos), 0)

class DistanseEstimator : 
    funcs = []
    
    def __add__(self, other):
        self.funcs += other.funcs
        return self

    def __init__(self, position, **kwargs):
        if "cube_size" in kwargs :
            self.funcs.append(lambda ray_pos : self.SimpleShapes.cube(position, kwargs["cube_size"], ray_pos))
        elif "ellipse_R" in kwargs :
            self.funcs.append(lambda ray_pos : self.SimpleShapes.ellipse(position, kwargs["ellipse_R"], ray_pos))

    def DE(self, position):
        return min(de(position) for de in self.funcs)

    class SimpleShapes :
        @staticmethod
        def md(vector):
            return sqrt(vector.dot(vector))

        @staticmethod
        def ellipse(position, R, ray_pos):
            md = DistanseEstimator.SimpleShapes.md
            return md(ray_pos - position) - R

        @staticmethod
        def cube(position, a, ray_pos):
            return max(map(abs, ray_pos - position)) - a/2

def getImage(x, y, DE, camera_pos, camera_rotation) : 
    traysing = MergeTraysing(camera_pos, (x, y), camera_rotation, DE)
    ret = Image.new("RGB", (x, y))
    for Y in range(y) :
        for X in range(x) :
            result = int(pow(traysing.start_ray(X, Y), 2)*255)
            ret.putpixel((X, Y), (result, result, result))
    return ret