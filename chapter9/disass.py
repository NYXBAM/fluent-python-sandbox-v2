from dis import dis

def f1(a):
    print(a)
    print(b)

# f1(3) # NameError: name 'b' is not defined

b = 6
def f2(a):
    print(a)
    print(b)
    b = 9
    
# f2(3) # UnboundLocalError: cannot access local variable 'b' where it is not associated with a value

b = 6 
def f3(a):
    global b
    print(a)
    print(b)
    b = 9
    
f3(3) # 3, 6
print(b) # 9

dis(f1)
'''
  3           RESUME                   0

  4           LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST                0 (a)
              CALL                     1
              POP_TOP

  5           LOAD_GLOBAL              1 (print + NULL)
              LOAD_GLOBAL              2 (b)
              CALL                     1
              POP_TOP
              RETURN_CONST             0 (None)
'''

dis(f2)

'''
10           RESUME                   0

 11           LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST                0 (a)
              CALL                     1
              POP_TOP

 12           LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST_CHECK          1 (b)
              CALL                     1
              POP_TOP

 13           LOAD_CONST               1 (9)
              STORE_FAST               1 (b)
              RETURN_CONST             0 (None)
'''