import abc
import re


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self,iterable):
        """Add items from an iterable."""
        pass
    
    @abc.abstractmethod
    def pick(self):
        """Remove item at random and return it. Raise LookupError if empty."""
        pass
    
    def loaded(self):
        """Return True if there are items in the container."""
        return bool(self.inspect())
    
    def inspect(self):
        items = []
        while True:
            try: 
                items.append(self.pick())
            except LookupError:
                break
            
        self.load(items)
        return tuple(items)