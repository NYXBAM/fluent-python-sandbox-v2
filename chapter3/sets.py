l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(set(l)) # {'spam', 'bacon', 'eggs'}
print(list(set(l))) # ['spam', 'bacon', 'eggs']


print(dict.fromkeys(l).keys()) # dict_keys(['spam', 'eggs', 'bacon'])
print(list(dict.fromkeys(l).keys())) # ['spam', 'eggs', 'bacon']

 
needles = 1,2,3,4,5,6,7,8
haystack = 2,3

found = len(set(needles) & set(haystack))

print(found) # 2