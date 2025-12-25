import re
from traceback import print_stack
import unicodedata
import string

def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    
    return unicodedata.normalize('NFC', shaved)

order = '"Herr Voß: • 1⁄2 cup of OEtkerTM caffè latte • bowl of açaí."'
print(shave_marks(order)) # "Herr Voß: • 1⁄2 cup of OEtkerTM caffe latte • bowl of acai."

Greek = 'Ζέφυρος, Zéfiro'

print(shave_marks(Greek)) # Ζεφυρος, Zefiro

def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c):
            continue
        preserve.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    
    return unicodedata.normalize('NFC', shaved)


