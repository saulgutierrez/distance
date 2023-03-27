# Python3 program to find Euclidean distance

# import numpy library
import numpy as np

# Driver Code
a = np.array((22, 2, 42, 11))
b = np.array((20, 1, 36, 9))

dist = np.linalg.norm(a-b)

print(dist)