from random import randrange

from tombola import Tombola

@Tombola.register
class TombolaList(list):
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
    
