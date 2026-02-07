def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco 
def target():
    print('running target()')
    

target() # running inner()
print(target) #  <function deco.<locals>.inner at 0x1073a3740>