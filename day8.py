# import numpy as np 
# x = np.zeros(5)
# print(x)

# x = np.ones(5)
# print(x)

# ar = np.arange(1,10,2)
# print(ar)

# ls = np.linspace(1,10,4)
# print(ls)

# arr = np.arange(1,7)
# print(arr)

# newarr = arr.reshape(3,2)
# print(newarr)

# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr.ndim)

import numpy as np
list = np.array([1,10,23,45,7])
print(max(list))
print(min(list))
print(sum(list))
print(sorted(list))
print(list.copy())
print(list.view())
print(np.sqrt(list))
print(list.mean())
print(np.unique(list))