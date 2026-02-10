import functools
from clockdeco import clock


@functools.cache # or @functools.lru_cache(maxsize=None) for older versions of Python, but lru_cache has maxsize parameter, while cache does not, and cache is more straightforward for memoization.
@clock 
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))
    
# without memoization, the number of calls grows exponentially with n, and the time taken grows accordingly. The output shows the time taken for each call to fibonacci, and the final result is 8 for fibonacci(6).
'''
[0.00000056s] fibonacci(0) -> 0
[0.00000068s] fibonacci(1) -> 1
[0.00007615s] fibonacci(2) -> 1
[0.00000021s] fibonacci(1) -> 1
[0.00000019s] fibonacci(0) -> 0
[0.00000023s] fibonacci(1) -> 1
[0.00000952s] fibonacci(2) -> 1
[0.00001945s] fibonacci(3) -> 2
[0.00010901s] fibonacci(4) -> 3
[0.00000018s] fibonacci(1) -> 1
[0.00000018s] fibonacci(0) -> 0
[0.00000023s] fibonacci(1) -> 1
[0.00000909s] fibonacci(2) -> 1
[0.00003273s] fibonacci(3) -> 2
[0.00000033s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00001687s] fibonacci(2) -> 1
[0.00000020s] fibonacci(1) -> 1
[0.00000019s] fibonacci(0) -> 0
[0.00000021s] fibonacci(1) -> 1
[0.00000904s] fibonacci(2) -> 1
[0.00001735s] fibonacci(3) -> 2
[0.00004297s] fibonacci(4) -> 3
[0.00012951s] fibonacci(5) -> 5
[0.00024918s] fibonacci(6) -> 8
8
'''

'''
After adding memoization with functools.lru_cache.
or functools.cache in newest version Python


[0.00000047s] fibonacci(0) -> 0
[0.00000084s] fibonacci(1) -> 1
[0.00009865s] fibonacci(2) -> 1
[0.00000080s] fibonacci(3) -> 2
[0.00011781s] fibonacci(4) -> 3
[0.00000063s] fibonacci(5) -> 5
[0.00013457s] fibonacci(6) -> 8
8
'''