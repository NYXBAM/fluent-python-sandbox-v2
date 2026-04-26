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