import itertools
from chapter13.bingo import BingoCage
from chapter13.tombola import Tombola


class AddableBingoCage(BingoCage):
    def __call__(self):
        return self.pick()
    
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        return NotImplemented
            
    
    def __iadd__(self, other):
            if isinstance(other, Tombola):
                other_iterable = other.inspect()
            else:
                try:
                    other_iterable = iter(other)
                except TypeError:
                    self_cls = type(self).__name__
                    raise TypeError(f"right operand must be {self_cls} or an iterable")
            
            self.load(other_iterable)
            return self 


vowels = "AEIOU"

globe = AddableBingoCage(vowels)
print(globe.inspect()) # ('I', 'A', 'O', 'E', 'U')

print(globe.pick() in vowels) # True

print(len(globe.inspect())) # 4

globe2 = AddableBingoCage('XYZ')
globe3 = globe + globe2
print(len(globe3.inspect())) # 7
# void = globe + [10, 20]
# print(void) #     void = globe + [10, 20]
#            ~~~~~~^~~~~~~~~~
# TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'

globe_orig = globe
print(len(globe.inspect())) # 4

globe += globe2
print(len(globe.inspect())) # 7

globe += ['M','N']
print(len(globe.inspect())) # 9

print(globe is globe_orig) #True
# globe += 1 # TypeError: right operand must be AddableBingoCage or an iterable