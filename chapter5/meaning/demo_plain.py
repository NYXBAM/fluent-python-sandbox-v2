class DemoPlainClass:
    a: int
    b: float = 1.1
    c = "spam"
    
print(DemoPlainClass.__annotations__) # {'a': <class 'int'>, 'b': <class 'float'>}
# print(DemoPlainClass.a) # AttributeError: type object 'DemoPlainClass' has no attribute 'a'
print(DemoPlainClass.b) # 1.1