import keyword
from collections import abc


class FrozenJSON:
    def __new__(cls, arg):
        print(f"Called __new__ method with arg: {arg}")
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        print(f"Called __init__ with mapping: {mapping}")
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        print(f"Called __getattr__ with name: {name}")
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON(self.__data[name])

    def __dir__(self):
        return self.__data.keys()


# Test
raw_data = {
    "name": "John",
    "info": {"city": "Odessa", "mode": "admin", "design": "super"},
    "user": {"surname": "Testre", "DOB": "1992.18.10"},
}

frozen = FrozenJSON(raw_data)

print(frozen.info.mode)  # admin
