from collections import deque

dq = deque(range(10), maxlen=10)
print(dq) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3)
print(dq) # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-4)
print(dq)#  deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

dq.appendleft([11, 22, 33])
print(dq) # deque([[11, 22, 33], 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.append([-32,-32]) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, [-1, -2]], maxlen=10)
print(dq)




l = [25, 15, '15', '123', 12,32,5,34,1231,5, "1", '2', '3']
print(sorted(l, key=int)) # ['1', '2', '3', 5, 5, 12, 15, '15', 25, 32, 34, '123', 1231]


