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