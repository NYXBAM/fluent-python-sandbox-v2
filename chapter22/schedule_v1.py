import json

JSON_PATH = "data/osconfeed.json"


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<{self.__class__.__name__} serial={self.serial!r}>"  # type: ignore


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


records = load(JSON_PATH)
speaker = records["speaker.3471"]
print(speaker)  # <Record serial=3471> # type: ignore
print(speaker.name)  # Anna Martelli Ravenscroft # type: ignore
