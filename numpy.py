import numpy as np
 
b = np.empty(2, dtype = int)
print("Matrix b : \n", b)
 
a = np.empty([2, 2], dtype = int)
print("\nMatrix a : \n", a)

print(a*b) # matrix multiplication
 
c = np.empty([3, 3])
print("\nMatrix c : \n", c)
