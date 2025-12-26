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


in_str  = "‚ƒ„ˆ‹" + "''" + '""' + "•" + "–—" + "˜›" + " "
out_str = "'f\"^<" + "''" + '""' + "*" + "--" + "~>" + " "

single_map = str.maketrans(in_str, out_str)


multi_map = {
    ord('€'): 'EUR',
    ord('…'): '...',
    ord('Æ'): 'AE',
    ord('æ'): 'ae',
    ord('Œ'): 'OE',
    ord('œ'): 'oe',
    ord('™'): '(TM)',
    ord('‰'): '<per mille>', 
    ord('†'): '**',
    ord('‡'): '***',
}


print(multi_map)
multi_map.update(single_map)

def dewinize(txt):
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)


order = '"Herr Voß: • 1⁄2 cup of OEtkerTM caffè latte • bowl of açaí."'
print(dewinize(order)) # "Herr Voß: * 1⁄2 cup of OEtkerTM caffè latte * bowl of açaí."
print(asciize(order)) # "Herr Voss: * 1⁄2 cup of OEtkerTM caffe latte * bowl of acai."

