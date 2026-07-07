class Quantity:
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        instance.__dict__[self.storage_name] = value


class LineItem:
    weight = Quantity()
    price = Quantity()
