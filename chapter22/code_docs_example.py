class Foo:
    @property
    def bar(self):
        "the bar attr"
        return self.__dict__["bar"]

    @bar.setter
    def bar(self, value):
        self.__dict__["bat"] = value


# print(help(Foo.bar))
print(help(Foo))

"""
class Foo(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  bar
 |      the bar attr
"""
