d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
from collections import ChainMap
chain = ChainMap(d1, d2)
print(chain['a'])  # Output: 1
print(chain['c'])  # Output: 6
chain['c'] = -1
print(d1) # Output: {'a': 1, 'b': 3, 'c': -1}
print(d2) # {'a': 2, 'b': 4, 'c': 6}