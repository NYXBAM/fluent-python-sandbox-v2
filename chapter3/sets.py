l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(set(l)) # {'spam', 'bacon', 'eggs'}
print(list(set(l))) # ['spam', 'bacon', 'eggs']


print(dict.fromkeys(l).keys()) # dict_keys(['spam', 'eggs', 'bacon'])
print(list(dict.fromkeys(l).keys())) # ['spam', 'eggs', 'bacon']

 
needles = 1,2,3,4,5,6,7,8
haystack = 2,3

found = len(set(needles) & set(haystack))

print(found) # 2


# s & z 
s = set([1,2,3])
z = set([2,5,6])

print(s & z) # {2}

print(s | z) # {1, 2, 3, 5, 6}
print(s - z) # {1, 3}
print(z - s) # {5, 6}
print(z ^ s) # {1, 3, 5, 6}


d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50) 
print(d1.keys() & d2.keys()) # {'b', 'd'}

s = {'a', 'e', 'i'}
print(d1.keys() & s) # {'a'}
print(d1.keys() | s) # # {'c', 'b', 'a', 'i', 'e', 'd'}