import time
from clockdeco0 import clock



@clock
def snooze(seconds):
    time.sleep(seconds)
    
    
@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print(f'6! = {factorial(6)}')
    
    
'''
**************************************** Calling snooze(.123)
[0.12756010s] snooze(0.123) -> None
**************************************** Calling factorial(6)
[0.00000125s] factorial(1) -> 1
[0.00002793s] factorial(2) -> 2
[0.00003972s] factorial(3) -> 6
[0.00004898s] factorial(4) -> 24
[0.00005907s] factorial(5) -> 120
[0.00007036s] factorial(6) -> 720
6! = 720
'''