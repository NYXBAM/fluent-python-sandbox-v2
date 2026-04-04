import math
from chapter12.vector_v5 import Vector

# I am trying to patching new methods

def __abs__(self):
    return math.hypot(*self)

def __neg__(self):
    return Vector(-x for x in self)

def __pos__(self):
    return Vector(self) # In book here was mistake,
                        # -Vector(self) was written, but it is wrong, because __neg__ is not defined yet, 
                        # so it will cause infinite recursion
# PATCHING 
Vector.__abs__ = __abs__ # type: ignore
Vector.__neg__ = __neg__ # type: ignore
Vector.__pos__ = __pos__ # type: ignore

v1 = Vector([1, 2, 3])

print(-v1) # type: ignore # (-1.0, -2.0, -3.0) # Works fine 
