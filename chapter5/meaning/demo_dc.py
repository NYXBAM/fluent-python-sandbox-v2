from dataclasses import dataclass


@dataclass() 
class DemoDataClass:
    a: int
    b: float = 1.1
    c = "spam"
    
    
print(DemoDataClass.__annotations__) # {'a': <class 'int'>, 'b': <class 'float'>}
print(DemoDataClass.__doc__) # DemoDataClass(a: int, b: float = 1.1)
print(DemoDataClass.b) # 1.1


dc = DemoDataClass(9)
print(dc.a) # 9

dc.a = 2399

print(dc.a)
dc.c = 'whatever'
print(dc.c) # whatever