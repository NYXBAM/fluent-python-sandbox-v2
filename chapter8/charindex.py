import sys 
import re
import unicodedata

from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1 

def tokenize(text: str) -> Iterator[str]:
    for match in RE_WORD.finditer(text):
        yield match.group().upper()
        
def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index

index = name_index(32, 65)

print(index)
'''
{'SPACE': {' '}, 'EXCLAMATION': {'!'}, 'MARK': {'!', '?', '"'}, 
'QUOTATION': {'"'}, 'NUMBER': {'#'}, 'SIGN': {'$', '%', '>', '=', '+', '#', '<'}, 
'DOLLAR': {'$'}, 'PERCENT': {'%'}, 'AMPERSAND': {'&'},
'APOSTROPHE': {"'"}, 'LEFT': {'('}, 'PARENTHESIS': {'(', ')'}, 
'RIGHT': {')'}, 'ASTERISK': {'*'}, 'PLUS': {'+'}, 
'COMMA': {','}, 'HYPHEN': {'-'}, 'MINUS': {'-'}, 
'FULL': {'.'}, 'STOP': {'.'}, 'SOLIDUS': {'/'}, 
'DIGIT': {'0', '3', '2', '8', '1', '5', '4', '7', '9', '6'}, 
'ZERO': {'0'}, 'ONE': {'1'}, 'TWO': {'2'}, 'THREE': {'3'}, 
'FOUR': {'4'}, 'FIVE': {'5'}, 'SIX': {'6'}, 'SEVEN': {'7'}, 
'EIGHT': {'8'}, 'NINE': {'9'}, 'COLON': {':'}, 
'SEMICOLON': {';'}, 'LESS': {'<'}, 'THAN': {'>', '<'}, 
'EQUALS': {'='}, 'GREATER': {'>'}, 'QUESTION': {'?'}, 
'COMMERCIAL': {'@'}, 'AT': {'@'}}
'''
print(index['SIGN']) # {'+', '>', '%', '#', '$', '<', '='}
print(index['DIGIT'] & index['EIGHT']) # {'8'}

