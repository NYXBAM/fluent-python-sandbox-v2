from random import randrange

from tombola import Tombola

@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pick from empty TombolaList')
    
    load = list.extend
    
    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(self)
    
# Tombola.register(TomboList)

t = TomboList(range(100))
print(isinstance(t, Tombola)) # True
print(dir(list))

print(TomboList.__mro__) # (<class '__main__.TomboList'>, <class 'list'>, <class 'object'>)
