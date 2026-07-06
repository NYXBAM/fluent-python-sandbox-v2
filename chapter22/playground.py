class Class:
    data = "the class data attr"

    @property
    def prop(self):
        return "the prop value"


obj = Class()
print(vars(obj))  # {}
print(obj.data)  # the class data attr
obj.data = "bar"
print(vars(obj))  # {'data': 'bar'}
print(obj.data)  # bar
print(Class.data)  # the class data attr

print(Class.prop)  # <property object at 0x103391490>
print(obj.prop)  # the prop value
# obj.prop = "FOO"  # AttributeError: property 'prop' of 'Class' object has no setter
obj.__dict__["prop"] = "foo"
print(vars(obj))  # {'data': 'bar', 'prop': 'foo'}
print(obj.prop)  # the prop value
Class.prop = "baz"
print(obj.prop)  # foo


print(obj.data)  # bar
print(Class.data)  # the class data attr
Class.data = property(lambda self: 'the "data" prop value')
print(obj.data)  # the "data" prop value
del Class.data
print(obj.data)  # bar


print(type(obj))
print(obj.__class__)

print(dir(obj))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__',
# '__str__', '__subclasshook__', '__weakref__', 'data', 'prop']
