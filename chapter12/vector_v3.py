from array import array 
import operator
import reprlib
import math 

class Vector:
    typecode = 'd'
    __match_args__ = ('x', 'y', 'z', 't')
    
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
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]
            
    def __getattr__(self, name):
        cls = type(self)
        error = None
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)
    
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = f'readonly attribute {name!r}'
            elif name.islower():
                error = 'can`t set attributes \'a\' to \'z\' in {cls.__name__!r}'
            else: error = ''   
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
            
        super().__setattr__(name, value)
        
        
    
# v = Vector(range(10))
# print(v.y, v.z) # 1.0 2.0

# print(v) # (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
# # v.x = 10 
# print(v.x) # 10
# print(v[0]) # 0.0
# print(v.__dict__) # {'_components': array('d', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]), 'x': 10}
# print(v) # (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)


# after adding __setattr__ method.
vs = Vector(range(10))
vs._components = array('d', range(5))
print(vs._components) # array('d', [0.0, 1.0, 2.0, 3.0, 4.0])
vs.some_field = 42 # OK 
vs.A = 42 # OK 

# 
try:
    vs.x = 777 
    vs.y = 777 
    print(vs.x, vs.y)
except Exception as e:
    print(e) # readonly attribute 'x'
    

