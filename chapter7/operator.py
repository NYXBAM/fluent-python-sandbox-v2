from collections import namedtuple
from functools import reduce
import operator

def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

# Better way, use reduce and operator.mul
from operator import mul, itemgetter

def factorial2(n):
    return reduce(mul, range(1, n+1))



# itemgetter

metro_data = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]


for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
# ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
# ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
# ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
# ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
 
cc_name = itemgetter(1,0) # We can put here any indexes

for city in metro_data:
    print(cc_name(city))
# ('JP', 'Tokyo')
# ('IN', 'Delhi NCR')
# ('MX', 'Mexico City')
# ('US', 'New York-Newark')
# ('BR', 'São Paulo')

# attrgetter 

LatLon = namedtuple("LatLon", "lat lon")
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
               for name, cc, pop, (lat, lon) in metro_data]

print(metro_areas[0]) # Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLon(lat=35.689722, lon=139.691667))
print(metro_areas[0].coord.lat) # 35.689722

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat') # show this tuple in example below

for city in sorted(metro_areas, key=attrgetter('pop')):
    print(name_lat(city)) # using attrgetter only to show name and coord.lat

# ('São Paulo', -23.547778)
# ('Mexico City', 19.433333)
# ('Delhi NCR', 28.613889)
# ('Tokyo', 35.689722)
# ('New York-Newark', 40.808611)

# all list func in module Operator

print([name for name in dir(operator) if not name.startswith('_')])
# ['abs', 'add', 'and_', 'attrgetter', 'call', 'concat', 'contains', 
#  'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd',
#  'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 
#  'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 
#  'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 
#  'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_',
#  'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']

# Example methodcaller func
from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s)) # THE TIME HAS COME
hyphenate = methodcaller('replace', ' ', '-')
print(hyphenate(s)) #The-time-has-come
