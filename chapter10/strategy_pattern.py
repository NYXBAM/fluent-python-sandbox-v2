from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional

class Customer(NamedTuple):
    name: str
    fidelity: int
    
class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal
    
    def total(self) -> Decimal:
        return self.price * self.quantity
    
class Order(NamedTuple): # Context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional["Promotion"] = None
    
    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self) -> str:
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
    
class Promotion(ABC): # Strategy: an abstract base class
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return the discount as a positive decimal value"""
        
class FidelityPromo(Promotion): # First Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)
    
    
class BulkItemPromo(Promotion): # Second Concrete Strategy
    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount
    
class LargeOrderPromo(Promotion): # Third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)
    

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = (LineItem('banana', 4, Decimal('0.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal('5.0')))

print(Order(joe, cart, FidelityPromo())) # <Order total: 42.00 due: 42.00>
print(Order(ann, cart, FidelityPromo())) # <Order total: 42.00 due: 39.90> # 5% discount for Ann because of her fidelity points

banana_cart = (LineItem('banana', 30, Decimal('0.5')),
                LineItem('apple', 10, Decimal('1.5')))

print(Order(joe, banana_cart, BulkItemPromo())) # <Order total: 30.00 due: 28.50> # 10% discount for bananas because of the quantity

long_cart = tuple(LineItem(str(sku), 1, Decimal(1))
                           for sku in range(10))
print(Order(joe, long_cart, LargeOrderPromo())) # <Order total: 10.00 due: 9.30> # 7% discount for 10 distinct items
print(Order(joe, cart, LargeOrderPromo())) # <Order total: 42.00 due: 42.00> # no discount because there are only 3 distinct items in the cart
