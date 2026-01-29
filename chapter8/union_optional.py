
# In python 3.10 we can use 
# str | bytes , instead Union[str, bytes]
# or str | None instead Optional[str]
# This version is shorter and more understandable

# Some example:


from typing import Union

def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token

# Python > 3.9
def tokenize(text: str) -> list[str]: # return list with each element str
    return text.upper().split()

# for example
# `stuff: list` is the same of stuff: `list[Any]`


# func tokenize in older version Python >=3.7

# from __future__ import annotations # didn't exist in 3.6

def tokenize_old(text: str) -> list[str]:
    return text.upper().split()


# Python >=3.5
from typing import List

def tokenize_older(text: str) -> List[str]:
    return text.upper().split()