# without list comprehension

symbols = '$%^&*&^%$$%^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes) # [36, 37, 94, 38, 42, 38, 94, 37, 36, 36, 37, 94]


# using lst comprehension
symbols = '¡™£¢∞§¶•ªº–ß$%^&*&^%$$%^'

codes = [ord(symbol) for symbol in symbols]
print(codes) #  [36, 37, 94, 38, 42, 38, 94, 37, 36, 36, 37, 94]

x = 'ABC'
codes = [ord(x) for x in x]
print(x) # ABC
print(codes) # [65, 66, 67]
codes = [last := ord(c) for c in x]
print(last) # 67


# map & filter vs listcomp

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)  # [161, 8482, 163, 162, 8734, 167, 182, 8226, 170, 186, 8211, 223]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii) # [161, 8482, 163, 162, 8734, 167, 182, 8226, 170, 186, 8211, 223]
 


# Decarts lists 

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts) # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
for color in colors:
    for size in sizes:
        print((color, size))
'''
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
'''
        
tshirts = [(color, size) for size in sizes
           for color in colors]
print(tshirts) # [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]
