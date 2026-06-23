from collections import abc 
import json 


class FrozenJSON: 
    def __init__(self, mapping):
        self.__data = dict(mapping)
        
    def __getattr__(self, name):
        try: 
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON.build(self.__data[name])
    
    def __dir__(self):
        return self.__data.keys()
    
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj 

raw_feed = json.load(open('data/osconfeed.json'))
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.speakers)) # 357 
print(feed.keys()) # dict_keys(['Schedule'])
print(sorted(feed.Schedule.keys()))  # ['conferences', 'events', 'speakers', 'venues']
print(feed.Schedule.conferences[0].serial)
print(feed.Schedule.speakers)
for speaker in feed.Schedule.speakers:
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


for key, value in sorted(feed.Schedule.items()):
    print(f'{len(value):3} {key}')
    
"""  
1 conferences
484 events
357 speakers
53 venues
"""