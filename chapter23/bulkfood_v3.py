class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            msg = f"{self.storage_name} must be > 0"
            raise ValueError(msg)

    def __get__(self, instance, owner):
        return instance.__dict__[self.storage_name]
