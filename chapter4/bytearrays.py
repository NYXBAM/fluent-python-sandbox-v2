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