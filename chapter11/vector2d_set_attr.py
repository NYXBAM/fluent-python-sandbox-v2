from vector2d_v3 import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd) # b'd\x9a\x99\x99\x99\x99\x99\xf1?\x9a\x99\x99\x99\x99\x99\x01@'
print(len(dumpd)) # 17
v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf) # b'f\xcd\xcc\x8c?\xcd\xcc\x0c@'
print(len(dumpf)) # 9
print(Vector2d.typecode) # d

class ShortVector2d(Vector2d):
    typecode = 'f'
    
    
sv = ShortVector2d(1/11, 1/27)
print(sv) # (0.09090909090909091, 0.037037037037037035)
print(len(bytes(sv))) # 9