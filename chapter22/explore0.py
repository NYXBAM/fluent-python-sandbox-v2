import json
from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

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
print(len(feed.Schedule.speakers))  # 357 # type: ignore
print(feed.keys())  # dict_keys(['Schedule']) # type: ignore
print(
    sorted(feed.Schedule.keys())  # type: ignore
)  # ['conferences', 'events', 'speakers', 'venues'] # type: ignore
print(feed.Schedule.conferences[0].serial)  # type: ignore# type: ignore
print(feed.Schedule.speakers)  # type: ignore
for speaker in feed.Schedule.speakers:  # type: ignore
    print(speaker.name)

"""
...
Frederic Berg
Tim Berglund
Andrew Berkowitz
Josh Berkus
Gina Blaber
Josh Bleecher Snyder
Michael Bleigh
Olivier Bloch
Adam Bordelon
Jay Borenstein
Joe Bowser
Garth Braithwaite
Alex Brandt
VM Brasseur
Tim Bray
Michael Brewer
Joe Brockmeier
Ethan Brown
Avi Bryant
Brian Bulkowski
Greg Bulmash
...
"""


for key, value in sorted(feed.Schedule.items()):  # type: ignore
    print(f"{len(value):3} {key}")

"""
1 conferences
484 events
357 speakers
53 venues
"""
