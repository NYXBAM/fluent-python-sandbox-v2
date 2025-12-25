s1 = 'cafe'
s2 = 'cafe\u0301' 
print(s1 == s2) # False 

from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


print(nfc_equal(s1, s2)) # True
print(nfc_equal('A', 'a')) # False 

s3 = 'Strase'
s4 = 'strasse'
print(s3 == s4) # False 

print(nfc_equal(s3, s4)) # False 
print(fold_equal(s3, s4)) # True 
print(fold_equal(s1, s2)) # True
print(fold_equal('A', 'a')) # True 