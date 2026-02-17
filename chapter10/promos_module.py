from decimal import Decimal
from func_strategy_pattern import Order
from func_strategy_pattern import (
    fidelity_promo, bulk_item_promo, large_order_promo
)
promos = [promo for name, promo in globals().items()
          if name.endswith('_promo') and
          name != 'best_promo'
          ]

def best_promo(order: Order) -> Decimal:
    return max(promo(order) for promo in promos)

