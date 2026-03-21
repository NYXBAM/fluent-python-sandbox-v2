import collections
import re

def _upper(key):
    try: 
        return key.upper()
    except AttributeError:
        return key
    
class UpperCaseMixin:
    def __setitem__(self, key, item):
        super().__setitem__(_upper(key), item) #  type: ignore[attr-defined]
        
    def __getitem__(self, key):
        return super().__getitem__(_upper(key)) # type: ignore[attr-defined]
    
    def get(self, key, default=None):
        return super().get(_upper(key), default) # type: ignore[attr-defined]
    
    def __contains__(self, key):
        return super().__contains__(_upper(key)) # type: ignore[attr-defined]
    
class UpperDict(UpperCaseMixin, collections.UserDict):
    pass

class UpperCounter(UpperCaseMixin, collections.Counter):
    """Counter class that uppercases keys"""


d = UpperDict([('a', 'letter A'), (2, 'digit two')])
print(list(d.keys())) # ['A', 2]
d['b'] = 'letter B'
print('b' in d) # True
print(d) # {'A': 'letter A', 2: 'digit two', 'B': 'letter B'}
print(d['a'], d.get('B')) # letter A letter B
print(list(d.keys())) # ['A', 2, 'B']

c = UpperCounter("BaNaNa")
print(c.most_common()) # [('A', 3), ('N', 2), ('B', 1)]
print(c) # UpperCounter({'A': 3, 'N': 2, 'B': 1})