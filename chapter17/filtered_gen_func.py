import itertools
# itertools compress 

items = ['Apple', 'Banana', 'Orange', 'Kiwi']

in_stock = [True, False, True, False]

available = itertools.compress(items, in_stock)
print(available) # <itertools.compress object at 0x10f6afee0>
print(list(available))  # ['Apple', 'Orange']


# itertools.dropwhille(predicate, it)

data = [0, 0, 0, 1, 2, 0, 3]
result = itertools.dropwhile(lambda x: x == 0, data)
print(list(result)) # [1, 2, 0, 3]
# drop all zero on beginning list



# filter(predicate, it)

nums = [1,2,3,4,5,6] 
evens = filter(lambda x: x % 2 == 0, nums)  # only evens
print(list(evens)) # [2,4,6] 

# itertools.filterfalse(predicate, it)
# reverse filter 
nums = [1,2,3,4,5,6]
odds = itertools.filterfalse(lambda x: x % 2 == 0, nums)
print(list(odds)) # [1,3,5]

# itertools.islice(it, start, stop, step)
nums = list(range(100))
short_list = itertools.islice(nums, 2, 99, 5)
print(list(short_list)) # [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]

# itertools.takewhile(predicate, it)

nums = [2, 5, 8, 12, 3 ,1]
result_takewhile = itertools.takewhile(lambda x: x < 10, nums)
print(list(result_takewhile)) # [2, 5, 8] # stopped in 12