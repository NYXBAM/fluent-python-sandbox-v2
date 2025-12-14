import collections


ct = collections.Counter('abracadabra')
print(ct) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaaazzzzz')
print(ct) # Counter({'a': 11, 'z': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(ct.most_common(3)) # [('a', 11), ('z', 5), ('b', 2)]
print(ct['a']) # 11
