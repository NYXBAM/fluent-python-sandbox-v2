def factorial(n):
    """Return n!"""
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(42)) # 1405006117752879898543142606244511569936384000000000
print(factorial.__doc__) # Return n!
print(type(factorial)) # <class 'function'>
fact = factorial
print(fact) # <function factorial at 0x107d36830>
print(map(factorial, range(11))) # <map object at 0x10193b280>
print(list(map(factorial, range(15)))) # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200]
