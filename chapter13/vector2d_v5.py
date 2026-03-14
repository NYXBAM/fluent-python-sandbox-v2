from array import array
import math
from typing import SupportsComplex, SupportsAbs


class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    # adding type hinting for __abs__ and __complex__
    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def __complex__(self) -> complex:
        return complex(self.x, self.y)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    @classmethod
    def fromcomplex(cls, datum: SupportsComplex) -> 'Vector2d':
        c = complex(datum)
        return cls(c.real, c.imag)
    



v = Vector2d(3, 4)

print(isinstance(v, SupportsComplex)) # True
print(isinstance(v, SupportsAbs)) # True

print(complex(v)) # (3+4j)
print(abs(v)) # 5.0
print(Vector2d.fromcomplex(3+4j)) # (3.0, 4.0)