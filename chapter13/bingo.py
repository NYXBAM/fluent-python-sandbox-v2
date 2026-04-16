import random 

from .tombola import Tombola

class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
        
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        """BUT WTF? Better `return self.pick()` instead of self.pick, otherwise it will return the method itself instead of the result of the method."""
        self.pick()
        
