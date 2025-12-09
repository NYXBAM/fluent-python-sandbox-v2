
tt = (1, 2, (30, 40))
print(hash(tt))  # -3907003130834322577

tl = (1, 2, ([30, 40]))
# print(hash(tl)) # TypeError: unhashable type: 'list'

tf = (1, 2, frozenset([30, 40]))
print(hash(tf)) # 5149391500123939311
