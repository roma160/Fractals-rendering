from PIL import Image
from numpy import matrix, sqrt, radians
import numpy as np

zero = 0.0001
camera_view_angle = 120

class Light:
    position = matrix([0, 0, 0])
    strength = 0

    def __init__(self, position, strength):
        self.position = position
        self.strength = strength

    #def calculate_ray(self, position):


class MergeTraysing :
    camera_pos = matrix([0, 0, 0])
    camera_size = matrix([0, 0])
    camera_rotation = matrix([0, 0])

    def __init__(self, camera_position, camera_size, camera_rotation, DE):
        self.camera_pos = camera_position
        self.camera_size = camera_size
        self.camera_rotation = camera_rotation
        self.DE = DE
        #self.lights = light

    def ray(self, position, last_pos) :
        min_dist = self.DE.DE(position)
        vect = position - last_pos
        last_pos = position
        position += vect * min_dist / vect.max()
        if(self.DE.DE(position) <= zero) :
            return 1 - self.DE.DE(position)/self.DE.DE(last_pos)
        else :
            return self.ray(self, position, last_pos)

    def start_ray(self, x, y) :
        min_delta = self.DE.DE(self.camera_pos)
        z_angle = radians(self.camera_rotation[0]) + np.arctan(
            (self.camera_size[0] - x)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size[0]
            )
        pos_x = self.camera_pos[0] + np.cos(z_angle)*min_delta
        pos_y = self.camera_pos[1] + np.sin(z_angle)*min_delta

        y_angle = radians(self.camera_rotation[1]) + np.arctan(
            (self.camera_size[1] - y)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size[1]
            )
        pos_z = self.camera_pos[3] + np.cos(y_angle)*min_delta
        return self.ray(matrix([pos_x, pos_y, pos_z]), self.camera_pos)

class DistanseEstimator : 
    funcs = []
    
    def __add__(self, other):
        self.funcs += other.funcs
        return self

    def __init__(self, position, **kwargs):
        if "cube_size" in kwargs :
            self.funcs += lambda ray_pos : self.SimpleShapes.cube(position, kwargs["cube_size"], ray_pos)
        elif "ellipse_R" in kwargs :
            self.funcs += lambda ray_pos : self.SimpleShapes.ellipse(position, kwargs["ellipse_R"], ray_pos)

    def DE(self, position):
        return min([de(position) for de in self.funcs])

    class SimpleShapes :
        @staticmethod
        def len(vector):
            return sqrt(vector @ vector)

        @staticmethod
        def ellipse(position, R, ray_pos):
            return len(ray_pos - position) - R

        @staticmethod
        def cube(position, a, ray_pos):
            return max(map(abs, ray_pos - position)) - a/2

