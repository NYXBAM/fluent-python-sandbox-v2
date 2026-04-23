def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')
    

res1 = [x*3 for x in gen_AB()]
# eager func

print(res1)
'''
start
continue
end.
['AAA', 'BBB']
'''
for i in res1:
    print('-->', i)
'''
--> AAA
--> BBB
'''

res2 = (x*3 for x in gen_AB())
# lazy evaluation
print(res2) # <generator object <genexpr> at 0x101c629b0>
for i in res2:
    print('-->', i)
'''
start
--> AAA
continue
--> BBB
end.
'''