import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing subtraction using arithmetic operator
sub_ans = a-b
print(sub_ans)

# Performing subtraction using numpy function
sub_ans = np.subtract(a, b)
print(sub_ans)
