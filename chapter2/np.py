import numpy as np 

a = np.arange(12)
print(a) # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(type(a)) # <class 'numpy.ndarray'>
print(a.shape) # (12,)
a.shape = 3, 4 
print(a) # 
"""
[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]]
"""
print(a[2]) # [ 8  9 10 11]]
print(a[2, 1]) # 9
print(a[:, 1]) # [1 5 9]
print(a.transpose())
"""
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
"""

import numpy 
floats = numpy.loadtxt('floats-10M.txt')
print(floats[-3:]) # [  0.98051748 526.63086773  84.99408007]
floats *= .5
print(floats[-3:]) # [  0.49025874 263.31543387  42.49704004]

from time import perf_counter as pc
t0 = pc(); floats /= 3; pc() - t0
numpy.save('floats-10M.txt', floats)
floats2 = numpy.load('floats-10M.txt.npy', 'r+')
floats *= 6
print(floats[-3:]) # [  0.98051748 526.63086773  84.99408007]
