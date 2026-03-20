from diamond import A

class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()
        

class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()
        
        
u = U()

# u.ping()  
"""
AttributeError: 'super' object has no attribute 'ping'
"""
leaf2 = LeafUA()
leaf2.ping()

"""
<instance of LeafUA>.ping() in LeafUA
<instance of LeafUA>.ping() in U
<instance of LeafUA>.ping() in A
<instance of LeafUA>.ping() in Root
"""