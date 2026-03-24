import functools
import operator
from collections.abc import Iterable
from typing import overload, Union, TypeVar

T = TypeVar('T')

# Book variant:
# S = TypeVar('S')

# Better variant:
S = TypeVar('S', int, float)
# We using a type variable S that is 
# constrained to int and float, which are the types that can be 
# used as the start value for the sum function.

@overload
def sum(it: Iterable[T], /) -> Union[T, int]: ...
@overload
def sum(it: Iterable[T], /, start: S) -> Union[T, S]: ...
def sum(it, /, start=0):
    return functools.reduce(operator.add, it, start)


# But this example is not very good. 


# print(sum([1,2,3,4], start='huy')) # TypeError: can only concatenate str (not "int") to str

