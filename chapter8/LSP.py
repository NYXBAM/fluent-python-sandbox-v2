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
f2(o1) # LSP.py:20: error: Argument 1 to "f2" has incompatible type "T1"; expected "T2"  [arg-type]
       # Found 1 error in 1 file (checked 1 source file)
       