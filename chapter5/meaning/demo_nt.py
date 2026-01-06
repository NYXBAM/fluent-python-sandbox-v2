import typing

class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = "spam"
    
print(DemoNTClass.__annotations__) # {'a': <class 'int'>, 'b': <class 'float'>}
print(DemoNTClass.a) # _tuplegetter(0, 'Alias for field number 0')
print(DemoNTClass.b) # _tuplegetter(1, 'Alias for field number 1')
print(DemoNTClass.c) # spam

nt = DemoNTClass(a=32029)
print(nt.b)  # 1.1

print(DemoNTClass.__doc__) # DemoNTClass(a, b)


