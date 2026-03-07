from collections import namedtuple, abc

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                      for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value
        
    def __delitem__(self, position):
        # The __delitem__ method is required by the MutableSequence ABC, but it is not
        del self._cards[position]
    
    def insert(self, position, value):
        # The insert method is required by the MutableSequence ABC, but it is not
        self._cards.insert(position, value)