import json
from typing import cast
from books import BookDict


# def from_json(data: str) -> BookDict:
#     whatever = json.loads(data)
#     return whatever

'''
 mypy books_any.py --disallow-any-expr
books.py:11: error: Incompatible types (expression has type "str", TypedDict item "authors" has type "list[str]")  [typeddict-item]
books_any.py:6: error: Expression has type "Any"  [misc]
books_any.py:7: error: Expression has type "Any"  [misc]
Found 3 errors in 2 files (checked 1 source file)

'''


# # the from_json with cast to BookDict

def from_json_cast(data: str) -> BookDict:
    whatever = cast(BookDict, json.loads(data))
    return whatever

"""
mypy books_any.py --disallow-any-expr
Success: no issues found in 1 source file
"""