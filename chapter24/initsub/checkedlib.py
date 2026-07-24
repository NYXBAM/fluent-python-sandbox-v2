from collections.abc import Callable
from copyreg import constructor
from typing import Any, NoReturn, get_type_hints

class Field:
    def __init__(self, name: str, constructor: Callable) -> None:
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f"{name!r} type hint must be callable")
        
        self.name = name 
        self.constructor = constructor
        
    def __set__(self, instance: Any, value: Any) -> None:
        if value is ...:
            value = self.constructor()
        else:
            try:
                value = self.constructor(value)
            except (TypeError, ValueError) as e:
                type_name = self.constructor.__name__
                msg = f'{value!r} is not compatible with {self.name}:{type_name}'
                raise TypeError(msg) from e 
        instance.__dict__[self.name] = value 
        

class Checked:
    @classmethod
    def _fields(cls) -> dict[str, type]:
        return get_type_hints(cls)
    
    
    def __init_subclass__(subcls) -> None:
        super().__init_subclass__()
        for name, constructor in subcls._fields().items():
            setattr(subcls, name, Field(name, constructor))
    
    def __init__(self, **kwargs: Any) -> None:
        for name in self._fields():
            value = kwargs.pop(name, ...)
            setattr(self, name, value)
            
        if kwargs:
            self.__flag_unknown_attrs(*kwargs)
            