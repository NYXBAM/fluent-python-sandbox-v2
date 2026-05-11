# some examples from contexlib. 

# # # # # # # # # # # #
# closing 
from contextlib import closing, suppress
from urllib.request import urlopen

with closing(urlopen('https://google.com')) as page:
    data = page.read()
    
# # # # # # # # # # # #
# suppress
# old version 
import os
try:
    os.remove('file.txt')
except FileNotFoundError:
    pass

# with supress
with suppress(FileNotFoundError):
    os.remove('file.txt')
    
# # # # # # # # # # # #
# ContextDecorator

from contextlib import ContextDecorator
import time 

class track_time(ContextDecorator):
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end = time.perf_counter()
        print(f"--- [END] Finished in {end - self.start:.4f}s ---")
        
# Now we can use this func in two ways: 

# like classic common context manager: 
# 1:  

with track_time():
    # do func 
    time.sleep(.5)

# Like decorator     
# 2: 
@track_time()
def my_heavy_func():
    print('Heavy working...')
    time.sleep(1)
  
my_heavy_func()


# # # # # # # # # # # #
# ExitStack 

# Bad idea: 
'''
with open('1.txt') as f1:
    with open('2.txt') as f2:
        with open('3.txt') as f3:
            # ... 
'''

# We can use ExitStack to avoid this pyramid of doom

from contextlib import ExitStack

files_to_open = ['data1.txt', 'data2.txt', 'data3.txt']
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in files_to_open]
    for f in files:
        print(f.read)



# # # # # # # # # # # #
# # # # # # # # # # # #