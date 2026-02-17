from decimal import Decimal
import inspect

from func_strategy_pattern import Customer, LineItem, Order
import promotions

promos = [func for _, func in inspect.getmembers(promotions,
                                                 inspect.isfunction)]


def best_promo(order: Order) -> Decimal:
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100) 

cart = [
    LineItem('banana', 30, Decimal('0.5')),
    LineItem('apple', 10, Decimal('1.5'))
]
order_joe = Order(joe, cart)
order_ann = Order(ann, cart)

print(Order(ann, cart, best_promo))  # <Order total: 30.00 due: 28.50>