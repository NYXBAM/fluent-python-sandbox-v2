from token import OP


class Pixel:
    __slots__ = ('x', 'y')
    
    
p = Pixel()
# print(p.__dict__)  # AttributeError: 'Pixel' object has no attribute '__dict__'.
p.x = 10
p.y = 20
# p.color = 'red' # AttributeError: 'Pixel' object has no attribute 'color' and no __dict__ for setting new attributes


class OpenPixel(Pixel):
    pass


op = OpenPixel()

print(op.__dict__) # {}

op.x = 8

print(op.__dict__)#  {}
print(op.x) # 8

op.color = 'green' 
print(op.__dict__) # {'color': 'green'}



class ColorPixel(Pixel):
    __slots__ = ('color',)
    
cp = ColorPixel() 
# print(cp.__dict__) # AttributeError: 'ColorPixel' object has no attribute '__dict__'
cp.x = 2
cp.color = 'blue'
# cp.flavor = 'banana'  # AttributeError: 'ColorPixel' object has no attribute 'flavor' and no __dict__ for setting new attributes

