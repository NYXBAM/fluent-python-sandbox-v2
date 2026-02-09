def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


avg = make_averager()
print(avg(10)) # 10.0
print(avg(11)) # 10.5   
print(avg(15)) # 12.0

print(avg.__code__.co_varnames) # ('new_value', 'total')
print(avg.__code__.co_freevars) # ('series',)
print(avg.__closure__) # (<cell at 0x7f8c9c1e5e80: list object at 0x7f8c9c1e5d00>,)
print(avg.__closure__[0].cell_contents) # [10, 11, 15]

# Not correct implementation of averager

def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        count += 1
        total += new_value
        return total / count
    return averager

avg = make_averager()
# print(avg(10)) # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

# Using nonlocal keyword
def make_averager_nonlocal():
    count = 0
    total = 0
    
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager


avg = make_averager_nonlocal()
print(avg(10)) # 10.0
print(avg(11)) # 10.5
print(avg(15)) # 12.0
# Now it's work properly because we use nonlocal keyword to modify the count and total variables in the enclosing scope.