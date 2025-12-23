import sys 
from unicodedata import name 

print(sys.version)
print() 
print('sys.stdout.isatty():', sys.stdout.isatty()) # sys.stdout.isatty(): True
print('sys.stdout.encoding:', sys.stdout.encoding) # sys.stdout.encoding: utf-8
print()

test_chars = [
    '\N{HORIZONTAL ELLIPSIS}',
    '\N{INFINITY}',
    '\N{CIRCLED NUMBER FORTY TWO}'
]
for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)
    '''
    Trying to output HORIZONTAL ELLIPSIS:
    …
    Trying to output INFINITY:
    ∞
    Trying to output CIRCLED NUMBER FORTY TWO:
    ㊷
    '''
