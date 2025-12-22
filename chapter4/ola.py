# coding: cp1252

print('Olá, Mundo!')

u16 = 'El Niño'.encode('utf_16')
print(u16)  # b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xc3\x00\xb1\x00o\x00'

print(list(u16)) # [255, 254, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 195, 0, 177, 0, 111, 0]
u16le = 'El Niño'.encode('utf_16le')
print(list(u16le)) # [69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 195, 0, 177, 0, 111, 0]
u16be = 'El Niño'.encode('utf_16be')
print(list(u16be)) # [0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 195, 0, 177, 0, 111] #