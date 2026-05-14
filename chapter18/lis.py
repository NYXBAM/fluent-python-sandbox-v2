
import math
import operator as op
from collections import ChainMap
from itertools import chain 
from typing import Any, TypeAlias, NoReturn

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol 
Expression: TypeAlias = Atom | list

def parse(program: str) -> Expression:
    return read_from_tokens(tokenize(program))

def tokenize(s: str) -> list[str]:
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens: list[str]) -> Expression:
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        exp = []
        while tokens[0] != ')':
            exp.append(read_from_tokens(tokens))
        tokens.pop(0)  # discard ')'
        return exp
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return parse_atom(token)

def parse_atom(token: str) -> Atom:
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


print(parse('1,5')) # 1,5 
print(parse('ni!')) # ni!
print(parse('(gcd 18 45)')) # ['gcd', 18, 45]
print(parse('''
            (define double
            (lambda (n)
            (* n 2)))
            '''))   # ['define', 'double', ['lambda', ['n'], ['*', 'n', 2]]]