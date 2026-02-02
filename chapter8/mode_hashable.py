from collections import Counter
from collections.abc import Iterable, Hashable
from typing import TypeVar

HashableT = TypeVar("HashableT", bound=Hashable)

def mode(data: Iterable[HashableT]) -> HashableT:
    "Using TypeVar with Hashable constraint"
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]

