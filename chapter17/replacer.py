from typing import TypeAlias
from collections.abc import Iterable

# FromTo = tuple[str, str]
FromTo: TypeAlias = tuple[str, str]


def zip_erplace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text