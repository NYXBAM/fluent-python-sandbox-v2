from collections.abc import Sequence

from chapter12.protocols_v0 import FrenchDeck




Sequence.register(FrenchDeck)

print(isinstance(FrenchDeck(), Sequence)) # True