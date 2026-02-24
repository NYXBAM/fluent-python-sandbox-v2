from array import array
import math


class Vector2d:
    __match_args__ = ('x', 'y')
    __slots__ = ('__x', '__y')
    
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
    
    def __abs__(self):
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
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    
    
'''
# Without slots 

time python3 mem_test.py vector2d_v3 Selected Vector2d type: vector2d_v3.Vector2d Creating 10,000,000 Vector2d instances Initial RAM usage: 6,983,680
 Final
RAM usage: 1,666,535,424
real 0m11.990s
user 0m10.861s
sys 0m0.978s


# using slots: 

time python3 mem_test.py vector2d_v3_slots Selected Vector2d type: vector2d_v3_slots.Vector2d Creating 10,000,000 Vector2d instances
Initial RAM usage: 6,995,968
Final
RAM usage: 577,839,104
real 0m8.381s user 0m8.006s sys 0m0.352s
'''