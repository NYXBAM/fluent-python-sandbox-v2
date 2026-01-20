def divmod(a, b, /):
    # / - >3.7 python to use positional-only args on left side
    return (a // b, a % b)

# print(divmod(a=11, b=12)) # 
print(divmod(11,12)) # (0, 11)


def divmod2(a, *, b):
    # * use to include named-only args
    return (a // b, a % b)


# print(divmod2(12,13))
print(divmod2(a=11,b=12))