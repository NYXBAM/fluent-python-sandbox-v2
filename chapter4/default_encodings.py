import locale 
import sys 


expressions = '''
locale.getpreferredencoding()
type(my_file) 
my_file.encoding 
sys.stdout.isatty()
sys.stdout.encoding 
sys.stdin.isatty() 
sys.stdin.encoding 
sys.stderr.isatty() 
sys.stderr.encoding 
sys.getdefaultencoding() 
sys.getfilesystemencoding()
'''

my_file = open('dummmy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(f'{expression:>30} -> {value!r}')
    
'''
 locale.getpreferredencoding() -> 'UTF-8'
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'UTF-8'
           sys.stdout.isatty() -> True
           sys.stdout.encoding -> 'utf-8'
            sys.stdin.isatty() -> True
            sys.stdin.encoding -> 'utf-8'
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'utf-8'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'utf-8'
'''