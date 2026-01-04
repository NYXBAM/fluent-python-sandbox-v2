class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
        
moscow = Coordinate(55.76, 37.62)
print(moscow)   #<__main__.Coordinate object at 0x10e3d4ec0>
location = Coordinate(55.76, 37.62)

print(location == moscow) # False 


from collections import namedtuple

Coordinate2 = namedtuple("Cooridnate", "lat lon")

print(issubclass(Coordinate2, tuple)) # True

moscow = Coordinate2(55.756, 37.617) 
print(moscow) # Cooridnate(lat=55.756, lon=37.617)
print(moscow == Coordinate2(lat=55.756, lon=37.617)) # True


import typing

Coordinate3 = typing.NamedTuple("Coordinate", [('lat', float), ('lon', float)])
print(issubclass(Coordinate3, tuple)) # True
print(typing.get_type_hints(Coordinate3)) # {'lat': <class 'float'>, 'lon': <class 'float'>}


from dataclasses import asdict, make_dataclass
from collections import namedtuple

DynamicNT = namedtuple('DynamicNT', 'id value')

DynamicDC = make_dataclass('DynamicDC', [('id', int), ('value', str)])

obj = DynamicDC(1, 'example')
nt_obj = DynamicNT(1, 'example')
print(obj) # DynamicDC(id=1, value='example')
print(nt_obj) # DynamicNT(id=1, value='example')
print(nt_obj._asdict())  # {'id': 1, 'value': 'example'}
print(obj.__dict__) # {'id': 1, 'value': 'example'}
print(asdict(obj)) # {'id': 1, 'value': 'example'}
