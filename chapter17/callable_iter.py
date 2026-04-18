from random import randint


def d6():
    return randint(1,6)

d6_iter = iter(d6, 1)

print(d6_iter) # <callable_iterator object at 0x10c59b400>
for roll in d6_iter:
    print(roll)
    
"""
3
4
6
2
3
2
3
3
6
2
6
4   
"""