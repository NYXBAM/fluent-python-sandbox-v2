

from typing import Generic, TypeVar
from chapter15.invariant import Beverage, Juice, OrangeJuice


T_co = TypeVar('T_co', covariant=True)

class BeverageDispenser(Generic[T_co]):
    def __init__(self, beverage: T_co) -> None:
        self._beverage = beverage
        
    def dispense(self) -> T_co:
        return self._beverage
    

def install(dispenser: BeverageDispenser[Juice]) -> None:
    ...
    
juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser) # No error: BeverageDispenser[OrangeJuice] is a subtype of BeverageDispenser[Juice]


beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser) # Error: incompatible types: BeverageDispenser[Beverage] is not BeverageDispenser[Juice]