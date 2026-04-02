from __future__ import annotations
from typing import TypeVar, Generic

class Refuse:
    '''All trash is a refuse.'''
    
class Biodegradable(Refuse):
    '''Biodegradable refuse.'''
    
class Compostable(Biodegradable):
    '''Compostable refuse.'''
    
T_contra = TypeVar('T_contra', contravariant=True)

class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        ...
def deploy(trash_can: TrashCan[Biodegradable]):
    ...
        
        
bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can) # No error: TrashCan[Refuse] is a subtype of TrashCan[Biodegradable]

compost_can: TrashCan[Compostable] = TrashCan()
deploy(compost_can) # Error: incompatible types: TrashCan[Compostable] is not TrashCan[Biodegradable]