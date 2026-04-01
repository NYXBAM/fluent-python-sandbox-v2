from __future__ import annotations
from typing import TypeVar, Generic


class Beverage:
    ...
    
class Juice(Beverage):
    ...
    
class OrangeJuice(Juice):
    ...
    
T = TypeVar('T')

class BeverageDispenser(Generic[T]):
    def __init__(self, beverage: T) -> None:
        self._beverage = beverage
        
    def dispense(self) -> T:
        return self._beverage
    
def install(dispenser: BeverageDispenser[Juice]) -> None:
    ...


juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser) # Error: incompatible types: BeverageDispenser[Beverage] is not BeverageDispenser[Juice]

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser) # Error: incompatible types: BeverageDispenser[OrangeJuice] is not BeverageDispenser[Juice]


