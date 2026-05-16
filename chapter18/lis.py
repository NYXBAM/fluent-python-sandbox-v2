
from itertools import chain
import math
import operator as op
from collections import ChainMap
from typing import Any, NoReturn, TypeAlias


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


class Environment(ChainMap[Symbol, Any]):
    def change(self, key: Symbol, value: Any) -> None: 
        for map in self.maps:
            if key in map:
                map[key] = value 
                return
        raise KeyError(key)
    

def standard_env() -> Environment:
    env = Environment()
    env.update(vars(math))
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        'abs': abs,
        'append': lambda *args: list(chain(*args)), 'apply': lambda proc, args: proc(*args), 'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'number?': lambda x: isinstance(x, (int, float)), 'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env


def repl(prompt: str = 'lis.py> ') -> NoReturn:
    global_env = Environment({}, standard_env())
    while True:
        ast = parse(input(prompt))
        val = evaluate(ast, global_env)
        if val is not None:
            print(lispstr(val))
            
def lispstr(exp: object) -> str:
    if isinstance(exp, list):
        return '(' + ' '.join(map(lispstr, exp)) + ')'
    else:
        return str(exp)



KEYWORDS = ['quote', 'if', 'lambda', 'define' 'set!']

def evaluate(exp: Expression, env: Environment) -> Any:
    match exp:
        case int(x) | float(x):
            return x 
        case Symbol(var):
            return env[var]
        case ['quote', x]:
            return x 
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        case ['define', Symbol(name), value_exp]:
            env[name] = evaluate(value_exp, env)
        case ['define', [Symbol(name), *params], *body] if body:
            env[name] = Procedure(params, body, env)
        case ['set!', Symbol(name), value_exp]:
            env.change(name, evaluate(value_exp, env))
        case [func_exp, *args] if func_exp not in KEYWORDS:
            proc = evaluate(func_exp, env)
            values = [evaluate(arg, env) for arg in args]
            return proc(*values)
        case _:
            raise SyntaxError(lispstr(exp))



print(parse('1,5')) # 1,5 
print(parse('ni!')) # ni!
print(parse('(gcd 18 45)')) # ['gcd', 18, 45]
print(parse('''
            (define double
            (lambda (n)
            (* n 2)))
            '''))   # ['define', 'double', ['lambda', ['n'], ['*', 'n', 2]]]

inner_env = {'a': 2}
outer_env = {'a': 0, 'b': 1}
env = Environment(inner_env, outer_env)
print(env['a']) # 2
env['a'] = 111
env['c'] = 222
print(env) # Environment({'a': 111, 'c': 222}, {'a': 0, 'b': 1})
env.change('b', 333)
print(env) # Environment({'a': 111, 'c': 222}, {'a': 0, 'b': 333})
