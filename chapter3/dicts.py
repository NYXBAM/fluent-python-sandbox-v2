d = dict(a=10, b=20, c=30)
values = d.values()
print(values) # dict_values([10, 20, 30])
print(list(values)) # [10, 20, 30]
print(reversed(values)) # <dict_reversevalueiterator object at 0x10799c590>
# print(values[0]) #TypeError: 'dict_values' object is not subscriptable
d['z'] = 99
print(d) # {'a': 10, 'b': 20, 'c': 30, 'z': 99}
print(values) # dict_values([10, 20, 30, 99])
