from array import array 
import operator
import reprlib
import math 

class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(self._components))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    
    # def __getitem__(self, index):
    #     return self._components[index]
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]
            
       
    
v1 = Vector([3,4,5,6])
print(len(v1)) # 4

print(v1[0], v1[-1]) # 3.0 6.0

v7 = Vector(range(7))
print(v7[1:4]) # array('d', [1.0, 2.0, 3.0])

# after adding new method __getitem__

v2 = Vector(range(20))
print(v2[1:5]) # (1.0, 2.0, 3.0, 4.0)
print(v2[-1]) # 19.0
# print(v2[1,2])# 
# , in __getitem__
# index = operator.index(key)
 