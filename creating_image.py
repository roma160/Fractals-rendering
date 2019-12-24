from PIL import Image
from numpy import array, sqrt, radians
import numpy as np
import time
from vec import *
import operator

zero = 0.0001
camera_view_angle = 100
max_iters = 5

def conv(x):
    if x != x:
        return 0
    elif x < 0:
        return 0
    else:
        return x

class MergeTraysing :
    camera_pos = vec3.create(0, 0, 0)
    camera_size = vec3.create(0, 0, 0)
    camera_rotation = vec3.create(0, 0, 0)

    def __init__(self, camera_position, camera_size, camera_rotation, DE):
        self.camera_pos = camera_position
        self.camera_size = camera_size
        self.camera_rotation = camera_rotation
        self.DE = DE
        #self.lights = light

    def ray(self, position, last_pos, iter) :
        min_dist = self.DE.DE(position)
        vect = position - last_pos
        last_pos = position
        position += vect.norm() * min_dist
        if iter > max_iters :
            return list(map(conv, (1 - self.DE.DE(position)/self.DE.DE(last_pos))*255))
        else :
            return self.ray(position, last_pos, iter + 1)

    def start_ray_fish(self, x, y) :
        min_delta = self.DE.DE(self.camera_pos)
        z_angle = radians(self.camera_rotation.comp()[0]) + np.arctan(
            2*(self.camera_size.comp()[0]/2 - x)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size.comp()[0]
            )
        y_angle = radians(self.camera_rotation.comp()[1]) + np.arctan(
            2*(self.camera_size.comp()[1]/2 - y)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size.comp()[1]
            )
        d_z = np.arctan(
            2*(self.camera_size.comp()[0]/2 - x)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size.comp()[0]
            ) + 0.0001# - radians(camera_view_angle/2)
        d_y = np.arctan(
            2*(self.camera_size.comp()[1]/2 - y)*
            np.tan(radians(camera_view_angle/2)) / self.camera_size.comp()[1]
            ) + 0.0001# - radians(camera_view_angle/2)

        actual_del = min_delta / (np.cos(d_z) * np.cos(d_y))
        
        pos_x = self.camera_pos.comp()[0] + np.cos(z_angle)*np.cos(y_angle)*actual_del
        pos_y = self.camera_pos.comp()[1] + np.sin(z_angle)*actual_del
        pos_z = self.camera_pos.comp()[2] + np.sin(y_angle)*actual_del
        return self.ray(vec3.create(pos_x, pos_y, pos_z), self.camera_pos, 0)

    def start_ray_ortogonal(self, x, y):
        min_delta = self.DE.DE(array(self.camera_pos))


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
        buff = list(de(position) for de in self.funcs)
        if buff[0].__class__.__name__ != "ndarray":
            return min(buff)
        else :
            return min(buff, key=tuple)

    class SimpleShapes :
        @staticmethod
        def ellipse(position, R, ray_pos):
            return sqrt(abs(ray_pos - position)) - R

        @staticmethod
        def cube(position, a, ray_pos):
            #return max(map(abs, ray_pos - position)) - a/2
            if ray_pos.x.__class__.__name__ != "ndarray":
                return max(map(abs, ray_pos.comp() - position.comp())) - a/2
            else :
                #return map(lambda x : max(map(abs, x.comp())) - a/2, ray_pos - position)
                return max(list(abs((ray_pos - position).comp()) - a/2), key=tuple)

def getImage(x, y, DE, camera_pos, camera_rotation) : 
    traysing = MergeTraysing(camera_pos, vec3.create(x, y, 0), camera_rotation, DE)
    ret = Image.new("L", (x, y))
    data = traysing.start_ray_fish(np.tile(np.arange(x), y), np.repeat(np.arange(y), x))
    ret.putdata(data)
    return ret