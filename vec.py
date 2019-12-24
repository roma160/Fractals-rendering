import numpy as np

class vec3 :
    @staticmethod
    def create(x, y, z):
        return vec3((x, y, z))
    @staticmethod
    def create_from_arrays(x, y, z):
        return np.array(list(map(lambda x, y, z : vec3.create(x, y, z), x, y, z)))
    def __init__(self, vect_arr):
        (self.x, self.y, self.z) = vect_arr
    def __mul__(self, other):
        return vec3((self.x * other, self.y * other, self.z * other))
    def __truediv__(self, other):
        return vec3((self.x / other, self.y / other, self.z / other))
    def __add__(self, other):
        if hasattr(other, "x") :
            return vec3((self.x + other.x, self.y + other.y, self.z + other.z))
        else :
            return vec3((self.x + other, self.y + other, self.z + other))
    def __sub__(self, other):
        if hasattr(other, "x") :
            return vec3((self.x - other.x, self.y - other.y, self.z - other.z))
        else :
            return vec3((self.x - other, self.y - other, self.z - other))
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def __abs__(self):
        return self.dot(self)
    def norm(self):
        mag = np.sqrt(abs(self))
        return self * (1.0 / np.where(mag == 0, 1, mag))
    def comp(self):
        return np.array((self.x, self.y, self.z))
    def abs(self):
        return vec3(abs(np.array((self.x, self.y, self.z))))
    def extract(self, cond):
        return vec3((extract(cond, self.x),
                    extract(cond, self.y),
                    extract(cond, self.z)))
    def make_array(self, size):
        return vec3.create(
            np.full(size, self.x),
            np.full(size, self.y),
            np.full(size, self.z)
        )