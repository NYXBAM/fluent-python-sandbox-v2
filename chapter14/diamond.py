class Root:
    def ping(self):
        print(f'{self}.ping() in Root')
        
    def pong(self):
        print(f'{self}.pong() in Root')
        
    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'
    

class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()
        
    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()
        
class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()
        
    def pong(self):
        print(f'{self}.pong() in B')

        

class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()
        
        
leaf1 = Leaf()
print(Leaf.__mro__)
# (<class '__main__.Leaf'>, 
# <class '__main__.A'>, 
# <class '__main__.B'>, 
# <class '__main__.Root'>, 
# <class 'object'>)
leaf1.ping()
"""
        <instance of Leaf>.ping() in Leaf
        <instance of Leaf>.ping() in A
        <instance of Leaf>.ping() in B
        <instance of Leaf>.ping() in Root
"""
leaf1.pong()
"""
        <instance of Leaf>.pong() in A
        <instance of Leaf>.pong() in B
"""