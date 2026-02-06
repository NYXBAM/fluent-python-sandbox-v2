# NoReturns Example 

from typing import NoReturn

def fail() -> NoReturn:
    raise ValueError("Oops")

def check_logic(x: int):
    if x < 0:
        fail() # NoReturn, after this point, the function will never return, so the rest of the code is unreachable
        print("This string is dead, and newer been used")  
    print('logic is correct')
    
    