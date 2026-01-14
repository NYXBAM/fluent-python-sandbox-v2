class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        
        
import copy

bus1 = Bus(["Alice", "Bill", "Claire", "David"])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1)) # 4448944080
print(id(bus2)) # 4448943648
print(id(bus3)) #  4448942832

bus1.drop("Bill")
print(bus2.passengers)
print(id(bus1.passengers)) # 4365254144
print(id(bus2.passengers)) # 4365254144
print(id(bus3.passengers)) # 4365250112
print(bus3.passengers)

a = [10, 20]
b = [a, 30]
a.append(b)
print(a) # [10, 20, [[...], 30]]
from copy import deepcopy
c = deepcopy(a)
print(c) # [10, 20, [[...], 30]]


def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x,y))
print(x, y)
a = [1, 2]
b = [3, 4]
print(f(a, b)) # [1, 2, 3, 4]
print(a, b) # [1, 2, 3, 4] [3, 4]

t = (10, 20)
u = (30, 40)
print(f(t,u)) # (10, 20, 30, 40)
print(t,u) # (10, 20) (30, 40)
