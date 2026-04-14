from collections import abc
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



# methods __matmul__, __rmatmul__
# dot product

# def __matmul__(self, other):
#     if (isinstance(other, abc.Sized) and 
#         isinstance(other, abc.Iterable)):
#         if len(self) == len(other):
#             return sum(a * b for a, b in zip(self, other))
#         else:
#             raise ValueError ('@ requires vectors of equal length')
#     else:
#         return NotImplemented
    
# From Python 3.10 zip using strict=True
def __matmul__(self, other):
    if isinstance(other, abc.Iterable): 
        try:
            # using strict = True 
            return sum(a * b for a, b in zip(self, other, strict=True))
        except ValueError:
            # if len != len 
            raise ValueError('@ requires vectors of equal length') from None
    else:
        return NotImplemented
    
def __rmatmul__(self, other):
    return self @ other


# eq 
# def __eq__(self, other):
#     return (len(self) == len(other) and 
#             all(a == b for a, b in zip(self, other)))


# Better way to avoud [1,2] == (1,2) # Fasle
def __eq__(self, other):
    if isinstance(other, Vector):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))
    else: 
        return NotImplemented 




# Monkey patching 

Vector.__add__ = __add__ # type: ignore
Vector.__radd__ = __radd__ # type: ignore
Vector.__mul__ = __mul__ # type: ignore
Vector.__rmul__ = __rmul__ # type: ignore
Vector.__matmul__ = __matmul__ # type: ignore 
Vector.__rmatmul__ = __rmatmul__ # type: ignore 
Vector.__eq__ = __eq__ # type: ignore


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



va = Vector([1, 2, 3])
vz = Vector([5, 6, 7])
print(va @ vz) # 38.0 
print(va @ vz == 38.0)# True # 1*5 + 2*6 + 3*7
print([10,20,30] @ vz) # 380.0

# print(va @ 3)   # TypeError: unsupported operand type(s) for @: 'Vector' and 'int'


# EQ 
vb = Vector(range(1,4))
print(va == vb) # True 

vc = Vector([1,2])

t3 = (1,2,3)
print(va == t3) # True 


# Augmented Assignment Operators

v1 = Vector([1, 2, 3])
v1_alias = v1 
print(id(v1)) # 4528247568

v1 += Vector([4,5,6])
print(v1) # (5.0, 7.0, 9.0)

print(id(v1)) # 4527422144
print(v1_alias) # (1.0, 2.0, 3.0)

v1 *= 11
print(v1) # (55.0, 77.0, 99.0)

print(id(v1)) # 4529021616