import weakref

s1 = {1, 2 ,3}
s2 = s1

def bye():
    print('...like tears it the rain.')
    
ender = weakref.finalize(s1, bye)
print(ender.alive) # True 
del s1 
print(ender.alive) # True 
s2 = 'spam'
# ...like tears it the rain.
print(ender.alive) # False

t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1) # True
t3 = t1[:]
print(t3 is t1) # True 


t1 = (1,2,3)
t3 = (1,2,3)
print(t3 is t1) # False

s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1) # True 