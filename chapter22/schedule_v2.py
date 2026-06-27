import inspect
import json

JSON_PATH = "data/osconfeed.json"


def load(path=JSON_PATH):
    records = {}
    with open(path, mode="r") as fp:
        raw_data = json.load(fp)
    for collection, raw_records in raw_data["Schedule"].items():  # type: ignore
        # record_type = collection[:-1]
        record_type = collection.removesuffix('s') # From python >=3.9
        for raw_record in raw_records:
            key = f"{record_type}.{raw_record['serial']}"
            records[key] = Record(**raw_record)
    return records

class Record:
    __index = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<{self.__class__.__name__} serial={self.serial!r}>"

    @staticmethod
    def fetch(key):
        if Record.__index is None:
            Record.__index = load()
        return Record.__index[key]

class Event(Record):
    
    def __repr__(self):
        try:
            return f"<{self.__class__.__name__} {self.name!r}>"
        except AttributeError:
            return super().__repr__()
        
    @property
    def venue(self):
        key = f'venue.{self.venue_serial}'
        return self.__class__.fetch(key)