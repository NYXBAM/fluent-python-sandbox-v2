import itertools
from chapter12.vector_v5 import Vector


# reloading add operator in Vector

def __add__(self, other):
    pairs = itertools.zip_longest(self, other, fillvalue=0.0)
    return Vector(a + b for a, b in pairs)

def __radd__(self, other):
    return self + other


Vector.__add__ = __add__ # type: ignore


v1 = Vector([3,4,5,6])
v2 = Vector([1,2])
print(v1 + v2)  # type: ignore # <(4.0, 6.0, 5.0, 6.0)>

from chapter13.vector2d_v5 import Vector2d

v2d = Vector2d(1,2)
print(v1 + v2d) # (4.0, 6.0, 5.0, 6.0)

# print((10,20,30) + v1) 
#  can only concatenate tuple
# 
#  (not "Vector") to tuple

# __radd__ operator 

Vector.__radd__ = __radd__ # type: ignore


# print(v1 + 1) # 'int' object is not iterable