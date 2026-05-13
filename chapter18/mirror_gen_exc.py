import contextlib
import sys 

@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write
    
    def reverse_write(text) -> int:
        original_write(text[::-1])
        return len(text) # only to avoid mypy error in `sys.stdout.write`
        
        
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
            

@looking_glass() # it's work with deco
def verse():
    print('The time has come')
     
verse() # emoc sah emit ehT
print('Back to reallity') # Back to reallity

