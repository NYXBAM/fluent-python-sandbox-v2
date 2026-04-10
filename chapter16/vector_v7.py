import itertools
from chapter12.vector_v5 import Vector


# reloading add operator in Vector

# def __add__(self, other):
#     pairs = itertools.zip_longest(self, other, fillvalue=0.0)
#     return Vector(a + b for a, b in pairs)

# Version with exceptions
def __add__(self, other):
    try:
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
    except TypeError:
        return NotImplemented

def __radd__(self, other):
    return self + other

# def __mul__(self,scalar):
#     return Vector(n * scalar for n in self)

# def __rmul__(self, scalar):
#     return self * scalar

# with exception

def __mul__(self, scalar):
    try:
        factor = float(scalar)
    except TypeError:
        return NotImplemented
    return Vector(n * factor for n in self)

def __rmul__(self, scalar):
    return self * scalar
    
# Monkey patching 

Vector.__add__ = __add__ # type: ignore
Vector.__radd__ = __radd__ # type: ignore
Vector.__mul__ = __mul__ # type: ignore
Vector.__rmul__ = __rmul__ # type: ignore



v1 = Vector([3,4,5,6])
v2 = Vector([1,2])
print(v1 + v2)  # type: ignore # <(4.0, 6.0, 5.0, 6.0)>

from chapter13.vector2d_v5 import Vector2d

v2d = Vector2d(1,2)
print(v1 + v2d) # (4.0, 6.0, 5.0, 6.0) # type: ignore

# print((10,20,30) + v1) 
#  can only concatenate tuple
# 
#  (not "Vector") to tuple

# __radd__ operator 


# print(v1 + 1) # 'int' object is not iterable


v1 = Vector([1.0, 2.0, 3.0])
print(14 * v1) # (14.0, 28.0, 42.0)
print(v1 * True) # (1.0, 2.0, 3.0)
from fractions import Fraction
print(v1 * Fraction(1, 3)) # (0.3333333333333333, 0.6666666666666666, 1.0)