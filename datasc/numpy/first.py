import numpy as np

arr = np.array([1,2,3])
type(arr)
raa = np.array([2, 3, 4])

np.dot(arr, raa)
(arr * raa).sum()



arr = list(range(1000000))
raa = list(range(1000000, 2000000))
result = 0

for x, y in zip(arr, raa):
    result += x * y
    
(np.array(arr) * np.array(raa)).sum()







