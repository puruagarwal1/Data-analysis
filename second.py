import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing addition using arithmetic operator
add_ans = a+b
print(add_ans)

# Performing addition using numpy function
add_ans = np.add(a, b)
print(add_ans)

# The same functions and operations can be used for
# multiple matrices
c = np.array([1, 2, 3, 4])
add_ans = a+b+c
print(add_ans)

add_ans = np.add(a, b, c)
print(add_ans)
