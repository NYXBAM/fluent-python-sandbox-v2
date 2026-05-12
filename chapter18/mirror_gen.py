import contextlib 
import sys 

@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write
    
    def reverse_write(text: str) -> int:
        original_write(text[::-1])
        return len(text) # only to avoid mypy error
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
    
with looking_glass() as what:
    print("Alice, Kitty and Snowdrop")
    print(what)
    """
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    """
print('Back to normal') # Back to normal
