import dis


l = [1,2,3]
print(id(l)) # 4459259136
l *= 2
print(l) # [1, 2, 3, 1, 2, 3]
print(id(l)) # 4459259136

t = (1,2,3)
print(id(t)) # 4334119616
t *= 2
print(id(t)) # 4333708544

# t = (1, 2, [30, 40])
# t[2] += [50, 60]
# print(t)

"""
     in <module>
    t[2] += [50, 60]
TypeError: 'tuple' object does not support item assignment
    
"""
print(dis.dis("s[a] += b"))

"""
  1           0 LOAD_NAME                0 (s)
              2 LOAD_NAME                1 (a)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_NAME                2 (b)
             10 INPLACE_ADD
             12 ROT_THREE
             14 STORE_SUBSCR
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
None
"""


# sort and sorted 

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits)) # ['apple', 'banana', 'grape', 'raspberry']
print(fruits) # ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, reverse=True)) # ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len)) # ['grape', 'apple', 'banana', 'raspberry']
print(sorted(fruits, key=len, reverse=True)) # ['raspberry', 'banana', 'grape', 'apple']
fruits.sort()
print(fruits) # ['apple', 'banana', 'grape', 'raspberry']

### ARRAYS 

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1]) # 0.4874373873920117
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1]) # 0.4874373873920117
print(floats2 == floats) # True 

# print(floats2.tobytes()[:50])