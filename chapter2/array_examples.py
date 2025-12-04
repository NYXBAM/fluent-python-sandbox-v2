from array import array

octets = array('B', range(6))

m1 = memoryview(octets)
print(m1.tolist()) # [0, 1, 2, 3, 4, 5]

m2 = m1.cast("B", [2, 3])
print(m2.tolist()) # [[0, 1, 2], [3, 4, 5]]
m3 = m1.cast("B", [3, 2])
print(m3.tolist()) # [[0, 1], [2, 3], [4, 5]]
m2[1,1] = 22
m3[1,1] = 33
print(octets) # array('B', [0, 1, 2, 33, 22, 5])

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv)) # 5
print(memv[0]) # -2
memv_oct = memv.cast('B')
print(memv_oct.tolist()) # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
print(numbers) # array('h', [-2, -1, 1024, 1, 2])
