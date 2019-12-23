from PIL import Image
from numpy import matrix, sqrt

class Light:
    position = matrix([0, 0, 0])
    strength = 0
    def __init__(self, position, strength):
        self.position = position
        self.strength = strength

class MergeTraysing :
    camera_pos = matrix([0, 0, 0])
    camera_size = matrix([0, 0, 0])
    def __init__(self, camera_position, camera_size):
        self.camera_pos = camera_position
        self.camera_size = camera_size

    def ray(self, position, last_pos, DE_hit, lights) :
        delta = DE_hit(position)

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