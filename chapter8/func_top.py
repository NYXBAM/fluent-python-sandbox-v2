
from typing import Iterable, TypeVar

T = TypeVar("T")

def top(series: Iterable[T], length: int) -> list[T]:
    ordered = sorted(series, reverse=True) # Here we have mypy error: `Value of type variable "SupportsRichComparisonT" of "sorted" cannot be "T"Mypytype-var`
    return ordered[:length]
    
    
print(top([4,1,5,2,6,7,3], 3)) # [7, 6, 5]

l = 'mango pear apple kiwi banana'.split()
print(top(l, 3)) # ['pear', 'mabngo', 'kiwi']

l2 = [(len(s), s) for s in l]
print(l2) # [(5, 'mango'), (4, 'pear'), (5, 'apple'), (4, 'kiwi'), (6, 'banana')]

l = [object() for _ in range(4)]
print(l) # [<object object at 0x1049401f0>, <object object at 0x104940600>, <object object at 0x104940630>, <object object at 0x1049405e0>]
# print(sorted(l)) # TypeError: '<' not supported between instances of 'object' and 'object'

class Spam:
    def __init__(self, n): self.n = n
    def __lt__(self, other): return self.n < other.n
    def __repr__(self): return f'<Spam({self.n})>'

l = [Spam(n) for n in range(5, 0, -1)]
print(l) # [<Spam(5)>, <Spam(4)>, <Spam(3)>, <Spam(2)>, <Spam(1)>]
print(sorted(l)) # [<Spam(1)>, <Spam(2)>, <Spam(3)>, <Spam(4)>, <Spam(5)>]



## Using Protocol to fix mypy error

from comparable import SupportsLessThan

LT = TypeVar("LT", bound=SupportsLessThan)

def top_protocol(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True) 
    return ordered[:length]
    

