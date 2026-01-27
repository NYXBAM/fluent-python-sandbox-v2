from typing import Any


class T1:
    ...
    
class T2(T1):
    ...
    
def f1(p: T1) -> None:
    ...
    
o2 = T2()
f1(o2) # OK


# But 

def f2(p: T2) -> None:
    ...
    
o1 = T1()
# f2(o1) # LSP.py:20: error: Argument 1 to "f2" has incompatible type "T1"; expected "T2"  [arg-type]
#        # Found 1 error in 1 file (checked 1 source file)
       
       
def f3(p: Any) -> None:
    ...
    
o0 = object()
o1 = T1()
o2 = T2()

f3(o0) # OK
f3(o1) # OK
f3(o2) # OK

def f4():
    ...
    
o4 = f4()
f1(o4) # OK
f2(o4) # OK
f3(o4) # OK


