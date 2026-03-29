import json
from typing import TypedDict

class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int
    
# Not correct authors should be list[str], but this is just to show the type error
# pp = BookDict(title='Programming Pearls',
#               authors='Jon Bentley', # This is a type error, should be list[str]
#               isbn='0202131213',
#               pagecount=256)

# Correct way to create a BookDict instance
pp = BookDict(title='Programming Pearls',
              authors=['Jon Bentley'], # This is correct, authors is a list of strings
              isbn='0202131213',
              pagecount=256)

print(pp)  # {'title': 'Programming Pearls', 'authors': 'Jon Bentley', 'isbn': '0202131213', 'pagecount': 256}
print(type(pp)) # <class 'dict'>
# print(pp.title) # AttributeError: 'dict' object has no attribute 'title'
print(pp['title']) # Programming Pearls

print(BookDict.__annotations__) 
# {'isbn': <class 'str'>, 
# 'title': <class 'str'>, 
# 'authors': list[str], 
# 'pagecount': <class 'int'>}


AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'

def to_xml(book: BookDict) -> str:
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(
                AUTHOR_ELEMENT.format(n) for n in value
            )
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n</BOOK>'


# the from_json with annotations BookDict 

def from_json(data: str) -> BookDict:
    whatever: BookDict = json.loads(data)
    return whatever
