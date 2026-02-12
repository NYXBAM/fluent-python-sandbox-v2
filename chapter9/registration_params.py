from re import A


registry = set()

def register(active=True):
    def decorate(func):
        print('running register'
              f'(active={active})->decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')
    
@register()
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')
    
    
f1()
f2()
f3()
print(registry) # {<function f2 at 0x108788400>}
register()(f3) # we will add f3 to registry
# or
register(active=False)(f1) # we remove from registry
print(registry)  # {<function f2 at 0x10d9cc4a0>, <function f3 at 0x10d90f920>}