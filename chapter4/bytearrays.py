s = 'café' 
print(len(s)) # 4
b = s.encode('utf8') 
print(b) # b'caf\xc3\xa9'
print(len(b)) # 5 
print(b[0]) # 99
print(b.decode('utf8')) # café


cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0]) # 99
print(cafe[:1]) # b'c'

cafe_arr = bytearray(cafe)
print(cafe_arr) # bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:]) # bytearray(b'\xa9')

print(bytes([100,101,102])) # b'def'


s = "ABC"
print(type(s[0]))   # <class 'str'>
print(type(s[:1]))  # <class 'str'>
print(s[0] == s[:1]) #
print(s[:1])


my_list = [1,3,4,5,6,6]

print(type(my_list[:1]))  #class 'list'


import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)  #b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'


for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
    '''
    latin_1 b'El Ni\xf1o'
    utf_8   b'El Ni\xc3\xb1o'
    utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
    '''
    
city = 'São Paulo'
print(city.encode('utf_8')) # b'S\xc3\xa3o Paulo'
print(city.encode('utf_16')) # b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
print(city.encode('iso8859_1')) # b'S\xe3o Paulo'
# print(city.encode('cp437')) # UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
print(city.encode('cp437', errors='ignore')) # b'So Paulo'
print(city.encode('cp437', errors='replace')) # b'S?o Paulo'
print(city.encode('cp437', errors='xmlcharrefreplace')) # b'S&#227;o Paulo'


octets = b'Montr\xe9al'
print(octets.decode('cp1252')) # Montréal
print(octets.decode('iso8859_7'))  # Montrιal
print(octets.decode('koi8_r')) # MontrИal
# print(octets.decode('utf8')) #  'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
print(octets.decode('utf8', errors='replace'))  # Montr�al


s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s1,s2) # café café
print(len(s1)) # 4
print(len(s2)) # 5
print(s1 == s2) # False

from unicodedata import normalize, name

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'

print(len(normalize('NFC', s1)), len(normalize('NFC', s2))) # 4 4
print(len(normalize('NFD', s1)), len(normalize('NFD', s2))) # 5 5
print(normalize('NFC', s1) == normalize('NFC', s2)) # True

ohm = '\u2126'
print(name(ohm)) # OHM SIGN
ohm_c = normalize('NFC', ohm)
print(name(ohm_c)) # GREEK CAPITAL LETTER OMEGA
print(ohm == ohm_c) # False 
print(normalize('NFC', ohm) == normalize('NFC', ohm_c)) # True 
