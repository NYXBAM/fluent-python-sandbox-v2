from collections import namedtuple


City = namedtuple("City", "name country population coordinates", defaults=('Test', 'test', 'test', 'test'))
tokyo = City("Tokyo", "JP", 36.933, (35.6897, 139.6922))
print(tokyo) # City(name='Tokyo', country='JP', population=36.933, coordinates=(35.6897, 139.6922))
print(tokyo.population)# 36.933
print(tokyo.coordinates)# (35.6897, 139.6922)
print(tokyo[1]) #JP

print(City._fields) # ('name', 'country', 'population', 'coordinates')
print(type(tokyo))
print(type(City))


Coordinate = namedtuple("Coordinate", "lat lon")
delhi_data = ("Delhi NCR", "IN", 21.935, Coordinate(28.6139, 77.2090))
delhi = City._make(delhi_data)
print(delhi._asdict()) # {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Coordinate(lat=28.6139, lon=77.209)}

test_data = ("Test", "JS", "test", "test")
test = City._make(test_data)
print(test)

test_data2 = ("Test2", "CN")
test2 = City(*test_data2)
print(test2) # City(name='Test2', country='CN', population='test', coordinates='test')

import json

print(json.dumps(delhi._asdict())) # {"name": "Delhi NCR", "country": "IN", "population": 21.935, "coordinates": [28.6139, 77.209]}