import inspect
from typing import NamedTuple
import typing

class Coordinate(NamedTuple):
    lat: float
    lon: float
    
    
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"
    
print(issubclass(Coordinate, tuple)) # True 


msc = Coordinate(lat=12.3333, lon=33.132)
# Python 3.10
print(inspect.get_annotations(Coordinate)) # {'lat': <class 'float'>, 'lon': <class 'float'>}
# Older version Python
print(typing.get_type_hints(Coordinate)) # {'lat': <class 'float'>, 'lon': <class 'float'>}
