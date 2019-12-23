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

    def __init__(self, type):
        if type == "cube" :
            self.funcs += self.SimpleShapes.cube
        elif type == "ellipse" :
            self.funcs += self.SimpleShapes.ellipse

    #def DE(self, position):


    @staticmethod
    class SimpleShapes :
        def len(self, vector):
            return sqrt(vector @ vector)

        def ellipse(self, position, R, ray_pos):
            return self.len(ray_pos - position) - R

        def cube(self, position, a, ray_pos):
            return max(map(abs, ray_pos - position)) - a/2