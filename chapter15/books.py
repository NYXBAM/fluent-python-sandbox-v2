from typing import TypedDict

class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int
    

pp = BookDict(title='Programming Pearls',
              authors='Jon Bentley', # This is a type error, should be list[str]
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
