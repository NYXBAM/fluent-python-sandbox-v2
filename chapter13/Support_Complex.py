from typing import SupportsComplex
import numpy as np

c64 = np.complex128(3+4j)
print(isinstance(c64, complex)) # True 
# in new version numpy 
print(hasattr(complex, "__complex__")) # True
print(isinstance(c64, SupportsComplex)) # True 

c = complex(c64)
print(c) # (3+4j)
print(isinstance(c, SupportsComplex)) # True 
print(complex(c)) # (3+4j)

sample = [1+0j, np.complex64(1+0j), 1.0, np.float16(1.0), 1, np.uint8(1)]

print([isinstance(x, SupportsComplex) for x in sample])
# [True, True, False, False, False, False]
print([complex(x) for x in sample])
# [(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j)]