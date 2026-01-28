
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
