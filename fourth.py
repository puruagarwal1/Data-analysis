import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing division using arithmetic operators
div_ans = a/b
print(div_ans)

# Performing division using numpy functions
div_ans = np.divide(a, b)
print(div_ans)
