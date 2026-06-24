import json
import keyword
from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            try:
                return FrozenJSON.build(self.__data[name])
            except KeyError:
                raise AttributeError(
                    f"'{type(self).__name__}' object has no attribute '{name}'"
                )

    def __dir__(self):
        return self.__data.keys()

    def __len__(self):
        return len(self.__data)

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


raw_feed = json.load(open("data/osconfeed.json"))
feed = FrozenJSON(raw_feed)
