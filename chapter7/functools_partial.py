import functools
from operator import mul
from functools import partial, partialmethod
import unicodedata

triple = partial(mul, 3)
print(triple(7)) # 21

print(list(map(triple, range(1, 10)))) # [3, 6, 9, 12, 15, 18, 21, 24, 27]

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print(s1 == s2) # False 
print(nfc(s1) == nfc(s2)) # True 

from tag import tag

picture = partial(tag, 'img', class_='pic-frame')
print(picture(src='wumpus.jpeg'))# <img class="pic-frame" src="wumpus.jpeg" />
print(picture.func) # <function tag at 0x10c03c680>
print(picture.args) # ('img',)
print(picture.keywords) # {'class_': 'pic-frame'}

# func partialmethod work same way, but just using method instead args
print(partialmethod.__doc__) 
# Method descriptor with partial application of the given arguments
# and keywords.

# Supports wrapping existing descriptors and handles non-descriptor
# callables as instance methods.
