from vec import *
from numpy import *

buff = vec3.create(0, 2, 3)
a = array((buff, buff, buff))
print(list(
    map(lambda x : max(map(abs, x.comp())) - 1, a - buff))
)
print(max([array([1, 2, 3]), array([2, 3, 4]), array([2, 3, 4])]))
print(a.__class__.__name__)