from types import MappingProxyType


d = {1: "A"}

d_proxy = MappingProxyType(d)
print(d_proxy) # {1: 'A'}
print(d_proxy[1]) # A
# d_proxy[2] = 'X' # TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d_proxy) # {1: 'A', 2: 'B'}
print(d_proxy[2]) # B
