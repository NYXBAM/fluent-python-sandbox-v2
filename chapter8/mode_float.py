
from collections import Counter
from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

def mode(data: Iterable[float]) -> float:
    "Without using TypeVar"
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


# T = TypeVar("T") # Old method

def mode_typevar[T](data: Iterable[T]) -> T:
    "Using TypeVar new method Python 3.12+ "
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]



NumberT = TypeVar("NumberT", float, Decimal, Fraction)

def mode_number_T(data: Iterable[NumberT]) -> NumberT:
    "Using TypeVar with constraints for numeric types"
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]



print(mode_number_T(["red", "blue", "blue", "red", "green", "red", "red"])) # Work, but 
# Mypy will raise an error since the type is constrained to numeric types only

