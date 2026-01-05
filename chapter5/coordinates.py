from collections import namedtuple
from locale import currency


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


Coordinate = namedtuple("Coordinate", 'lat lon reference', defaults=["WGS84"])

print(Coordinate(0, 0)) # Coordinate(lat=0, lon=0, reference='WGS84')


# Namedtuple with methods 
        
from collections import namedtuple


Item = namedtuple('Item', ['name', 'price'])

iphone = Item('iPhone 15', 1000)
milk = Item('Moloko', 2)


def get_pretty_price(self):
    return f"${self.price}.00 USD"


def get_discount_price(self):
    return self.price * 0.9


Item.pretty_price = get_pretty_price
Item.discount = get_discount_price

print(f"{iphone.name} : {iphone.discount()}") 

print(Item.__dict__)

# Or better readable way 

class Item(namedtuple('Item', ['name', 'price'])):
    currency = '$'
    
    def pretty_price(self):
        return f"{self.currency}{self.price}.00"

    def discount(self, percent=10):
        return self.price * (1 - percent/100)
    
    