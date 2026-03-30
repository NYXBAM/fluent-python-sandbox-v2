from __future__ import annotations
import inspect
from typing import get_type_hints # for forward references


class Rectangle:
    def stretch(self, factor: float) -> Rectangle:
        return Rectangle()
    
print(Rectangle.stretch.__annotations__) # {'factor': 'float', 'return': 'Rectangle'}
print(get_type_hints(Rectangle.stretch)) # {'factor': <class 'float'>, 'return': <class '__main__.Rectangle'>}
print(inspect.get_annotations(Rectangle.stretch)) # {'factor': 'float', 'return': 'Rectangle'}
print(inspect.get_annotations(Rectangle.stretch, eval_str=True)) # {'factor': <class 'float'>, 'return': <class '__main__.Rectangle'>}