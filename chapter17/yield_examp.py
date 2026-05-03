from colorsys import yiq_to_rgb


def sub_gen():
    yield 1.1
    yield 1.2
    
def gen():
    yield 1
    for i in sub_gen():
        yield i 
    yield 2
    
for x in gen():
    print(x)
    
'''
1
1.1
1.2
2
'''

def sub_gen_1():
    yield 1.1
    yield 1.2
    return 'Done!'

def gen_1():
    yield 1
    result = yield from sub_gen_1()
    print('<--', result)
    
for x in gen_1():
    print(x)

'''
1
1.1
1.2
<-- Done!
'''

# Like itertools.chain

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i 
            
            
s = 'ABC'
r = range(3)
print(list(chain(s,r))) # ['A', 'B', 'C', 0, 1, 2]


# OR simple chain with yield from 
def chain_yield(*iterables):
    for i in iterables:
        yield from i
        
print(list(chain_yield(s,r))) # ['A', 'B', 'C', 0, 1, 2]