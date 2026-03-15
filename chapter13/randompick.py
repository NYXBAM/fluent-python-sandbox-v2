from typing import Protocol, runtime_checkable, Any

@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any: ...
    


print(getattr(RandomPicker, '_is_protocol')) # True 
print(dir(RandomPicker))
'''
True
['__abstractmethods__', '__annotations__', '__class__', 
'__class_getitem__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__non_callable_proto_members__', '__parameters__',
'__protocol_attrs__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__slots__', '__static_attributes__',
'__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_is_protocol', 
'_is_runtime_protocol', 'pick']
'''

