class Gizmo:
    def __init__(self):
        print(f"Gizmo id: {id(self)}")
        
x = Gizmo() # Gizmo id: 4416920816 
print(dir())
# ['Gizmo', '__annotations__', '__builtins__', '__cached__', 
# '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'x']

charles = {'name': "Charles L. Dogson", 'born': 1832}
lewis = charles
print(lewis is charles) # True 

print(id(charles)) # 4527061120
print(id(lewis)) # 4527061120
lewis['balance'] = 950
print(charles) # {'name': 'Charles L. Dogson', 'born': 1832, 'balance': 950}

alex = {'name': "Charles L. Dogson", 'born': 1832, 'balance': 950}
print(alex == charles) # True 
print(alex is not charles) # True
