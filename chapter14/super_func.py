from typing import OrderedDict


class UpdateOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        
class NotRecommended(OrderedDict):
    "Bad example of subclassing OrderedDict"
    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self.move_to_end(key)

class LastUpdateOrderedDict(OrderedDict):
    "Python2 compatible version of UpdateOrderedDict"
    def __setitem__(self, key, value):
        super(LastUpdateOrderedDict, self).__setitem__(key, value)
        self.move_to_end(key)