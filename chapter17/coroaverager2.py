from collections.abc import Generator
from typing import TypeAlias
from typing import Union, NamedTuple

class Result(NamedTuple):
    count: int # type: ignore
    average: float 
    
class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'
    
STOP = Sentinel()

# SendType = Union[float, Sentinel]
SendType: TypeAlias = float | Sentinel # Python 3.10

def averager2(verbose: bool=False) -> Generator[None, SendType, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if verbose:
            print('received', term)
        if isinstance(term, Sentinel):
            break 
        total += term
        count += 1 
        average = total / count 
    return Result(count, average)



coro_avg = averager2()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))

try: 
    coro_avg.send(STOP)
except StopIteration as e:
    print(e.value) # Result(count=3, average=15.0)