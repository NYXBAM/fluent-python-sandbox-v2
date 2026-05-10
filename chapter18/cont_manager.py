with open('mirror.py') as fp:
    src = fp.read(60)

    
    
print(len(src)) # 60
print(fp) # <_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
print(fp.closed, fp.encoding) # True UTF-8
# print(fp.read(60)) # ValueError: I/O operation on closed file.


from mirror import LookingGlass

with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    '''
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    '''
    
print(what) # JABBERWOCKY


# LookingGlass without context manager 

manager = LookingGlass()
print(manager) # <mirror.LookingGlass object at 0x10527b390>

monster = manager.__enter__()
print(monster == 'JABBERWOCKY') # eurT
print(monster) # YKCOWREBBAJ
print(manager) # >09376c101x0 ta tcejbo ssalGgnikooL.rorrim<
print(manager.__exit__(None, None, None))
print(monster) # JABBERWOCKY