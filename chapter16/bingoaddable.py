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
print(globe.inspect())