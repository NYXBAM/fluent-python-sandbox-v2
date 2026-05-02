import itertools
import operator
# itertools compress 

items = ['Apple', 'Banana', 'Orange', 'Kiwi']

in_stock = [True, False, True, False]

available = itertools.compress(items, in_stock)
print(available) # <itertools.compress object at 0x10f6afee0>
print(list(available))  # ['Apple', 'Orange']

##############################
# itertools.dropwhille(predicate, it)

data = [0, 0, 0, 1, 2, 0, 3]
result = itertools.dropwhile(lambda x: x == 0, data)
print(list(result)) # [1, 2, 0, 3]
# drop all zero on beginning list


##############################
# filter(predicate, it)

nums = [1,2,3,4,5,6] 
evens = filter(lambda x: x % 2 == 0, nums)  # only evens
print(list(evens)) # [2,4,6] 

##############################
# itertools.filterfalse(predicate, it)
# reverse filter 
nums = [1,2,3,4,5,6]
odds = itertools.filterfalse(lambda x: x % 2 == 0, nums)
print(list(odds)) # [1,3,5]

##############################
# itertools.islice(it, start, stop, step)
nums = list(range(100))
short_list = itertools.islice(nums, 2, 99, 5)
print(list(short_list)) # [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]

##############################
# itertools.takewhile(predicate, it)

nums = [2, 5, 8, 12, 3 ,1]
result_takewhile = itertools.takewhile(lambda x: x < 10, nums)
print(list(result_takewhile)) # [2, 5, 8] # stopped in 12

##############################
# itertools.accumulate(iterable, [func])

data = [1,2,3,4,5]

print(list(itertools.accumulate(data))) # (1, 1+2, 1+2+3)  # [1, 3, 6, 10, 15]
print(list(itertools.accumulate(data, operator.mul))) # [1, 2, 6, 24, 120]

def mult(a, other):
    
    return a * other
print(list(itertools.accumulate(data, mult))) # [1, 2, 6, 24, 120]
 
 
############################## 
# enumerate(iterable, start=0)

langs = ['Python','JS', 'Rust']
print(list(enumerate(langs))) # [(0, 'Python'), (1, 'JS'), (2, 'Rust')]

for num, name in enumerate(langs, start=1):
    print(f'{num}: {name}')
'''
1: Python
2: JS
3: Rust
'''

 
############################## 
# map(func, it1, [it2,...])

nums = [1,2,3,4]
print(list(map(lambda x: x**2, nums))) # [1, 4, 9, 16]

list_a = [1,2,3]
list_b = [10,20,30,40,50]


print(list(map(lambda x, y: x + y, list_a, list_b)))  # [11, 22, 33] 


############################## 
# itertools.starmap(func, iterable)

shapes = [(2,5), (3,2), (10,10)]
def area(w, h):
    return w * h

print(list(itertools.starmap(area,shapes))) # [10, 6, 100]

##############################
# itertools.chain(it1, it2, ...)

numbers = [1,2,3]
letters = ['a', 'b']

for item in itertools.chain(numbers, letters):
    print(item)

'''
1
2
3
a
b
'''
print(list(itertools.chain('ABC', range(2)))) # ['A', 'B', 'C', 0, 1]
print(list(itertools.chain(enumerate('ABC')))) # [(0, 'A'), (1, 'B'), (2, 'C')]
##############################
# itertools.chain.from_iterable(it)
matrix = [[1,2], [3,4], [5,6], [7,8,9],[10,11]]
flat = list(itertools.chain.from_iterable(matrix))
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(itertools.chain.from_iterable(enumerate('ABC')))) # [0, 'A', 1, 'B', 2, 'C']



##############################
# itertools.product(it1, it2, ..., repeat=1)
colors = ['red', 'blue']
sizes = ['S', 'M']
combinations = list(itertools.product(colors, sizes))
print(combinations)  #[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))
'''
[('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
'''
print(list(itertools.product(range(2), repeat=3))) # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

##############################
# zip(it1, ..., itN, strict=False)  # strict=True if len(it1) != len(itOther)

names = ["Alice", "Bob"]
scores = [100,85,90]
print(list(zip(names, scores))) # [('Alice', 100), ('Bob', 85)]
print(list(zip("ABC", range(5), [10,20,30,40]))) # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]

##############################
# itertools.zip_longest(it1, ..., fillvalue=None) 
from typing import Any # to avoid mypy errors

names: list[Any] = ["Alice", "Bob"]
scores: list[Any] = [100,85,90]
print(list(itertools.zip_longest(names, scores, fillvalue='NoScore'))) # [('Alice', 100), ('Bob', 85), ('NoScore', 90)]


##############################
# itertools.combinations(it, out_len)

print(list(itertools.combinations([1,2,3], 2)))
# [(1, 2), (1, 3), (2, 3)]
 
 
 ##############################
 # itertools.combinations_with_replacment(it, out_len)

print(list(itertools.combinations_with_replacement([1,2,], 2)))
 # [(1, 1), (1, 2), (2, 2)]


 ##############################
 # itertools.count(start=0, start=1)
for i in itertools.count(10,5):
     if i > 25: break
     print(i, end=' ') # 10 15 20 25 
     

 ##############################
 # itertools.cycle(it)
c = 0
for i in itertools.cycle("ABC"):
     if c == 5: break
     print(i, end=' ') # A B C A B
     c += 1
 
##############################
# itertools.pairwise(it)

print(list(itertools.pairwise([1, 2, 3, 4]))) #  [(1, 2), (2, 3), (3, 4)]


##############################
# itertools.permutations(it, out_len=None)
print(list(itertools.permutations([1,2], 2))) # [(1, 2), (2, 1)]

##############################
#itertools.repeat(item, [times])
print(list(itertools.repeat('Hi', 3)))  # ['Hi', 'Hi', 'Hi']


# some examples from book

def vowel(c):
    return c.lower() in 'aeiou'

print(list(filter(vowel, 'Aardvark'))) # ['A', 'a', 'a']

print(list(itertools.filterfalse(vowel, 'Aardvark'))) #['r', 'd', 'v', 'r', 'k']
print(list(itertools.dropwhile(vowel, 'Aardvark'))) # ['r', 'd', 'v', 'a', 'r', 'k']
print(list(itertools.takewhile(vowel, 'Aardvark'))) # ['A', 'a']
print(list(itertools.compress('Aardvark', (1,0,1,1,0,1)))) # ['A', 'r', 'd', 'a']

print(list(itertools.islice('Aardvark', 4))) # ['A', 'a', 'r', 'd']
print(list(itertools.islice('Aardvark', 4, 7)))  #  ['v', 'a', 'r']
print(list(itertools.islice('Aardvark', 1, 7, 2)))   # ['a', 'd', 'a']


sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample, min))) # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]

print(list(itertools.accumulate(sample, max))) # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
 
print(list(itertools.accumulate(range(1,11), operator.mul))) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

print(list(enumerate('albatroz', 1))) # [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]

print(list(map(operator.mul, range(11), range(11)))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


print(list(map(operator.mul, range(11), [2,4,8]))) # [0,4,16]
print(list(map(lambda a, b: (a, b), range(11), [2,4,8]))) # [(0, 2), (1, 4), (2, 8)]

print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))) # ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']

sample = [5,4,2,8,7,6,3,0,9,1]
print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1))))
# [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]


ct = itertools.count()
print(next(ct)) # 0
print(next(ct), next(ct), next(ct), next(ct)) # 1 2 3 4

print(list(itertools.islice(itertools.count(1, .3), 3))) # [1, 1.3, 1.6]

cy = itertools.cycle('ABC')
print(next(cy)) # A
print(list(itertools.islice(cy, 7))) # ['B', 'C', 'A', 'B', 'C', 'A', 'B']

print(list(itertools.pairwise(range(7)))) # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

rp = itertools.repeat(7)
print(next(rp), next(rp)) # 7 7
print(list(itertools.repeat(8, 4))) # [8, 8, 8, 8]

print(list(map(operator.mul, range(11), itertools.repeat(5))))
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(list(itertools.combinations('ABC', 2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.combinations_with_replacement('ABC', 2))) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(list(itertools.permutations("ABC", 2))) #[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(list(itertools.product('ABC', repeat=2))) #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
# product is 
# for i in "ABC":
    # for j in "ABC":
'''
result = []
for i in "ABC":          # Outer loop
    for j in "ABC":      # Inner loop
        result.append((i, j))

print(result)
'''
print(list(itertools.groupby("LLLLAAGGG")))
# [('L', <itertools._grouper object at 0x100c15e40>), ('A', <itertools._grouper object at 0x100c14880>), ('G', <itertools._grouper object at 0x100c16d10>)]

for char, group in itertools.groupby("LLLLAAGGG"):
    print(char, '->', list(group))    
'''
L -> ['L', 'L', 'L', 'L']
A -> ['A', 'A']
G -> ['G', 'G', 'G']
'''
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals) # ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
'''
7 -> ['dolphin', 'giraffe']
5 -> ['shark', 'eagle']
4 -> ['lion', 'bear', 'duck']
3 -> ['bat', 'rat']
'''
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
'''
3 -> ['rat', 'bat']
4 -> ['duck', 'bear', 'lion']
5 -> ['eagle', 'shark']
7 -> ['giraffe', 'dolphin']
'''

print(list(itertools.tee('ABC'))) # [<itertools._tee object at 0x102ddcc00>, <itertools._tee object at 0x102ddcbc0>]

g1, g2 = itertools.tee('ABC')
print(next(g1)) # A
print(next(g2)) # A
print(next(g2)) # B 
print(list(g1)) # ['B', 'C']
print(list(g2)) # ['C']

print(all([1,2,3])) # True 
print(all([1,0,3])) # False
print(all([])) # True 

print(any([1,2,3])) # True  
print(any([1,0,3])) # True 
print(any([0,0,0])) # False 
print(any([])) # False 

