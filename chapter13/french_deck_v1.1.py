import collections
from typing import Sequence

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                      for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
FD = FrenchDeck()

print(isinstance(FD, Sequence)) # False

from random import shuffle

deck = FrenchDeck()
# shuffle(deck) # TypeError: 'FrenchDeck' object does not support item assignment

# Monkey patching __setitem__ to make it work
def set_card(deck, position, card):
    deck._cards[position] = card 
    
    
FrenchDeck.__setitem__ = set_card
shuffle(deck) # No error now
print(deck[:5])