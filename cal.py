import numpy as np
from numpy.linalg import solve
a = np.array([[2, 2, 2, 1], [-1, -1, -3, -2], [1, 2, 5, 3], [-1, -2, -4, -2]]).reshape(4, 4)
b= np.array([0,0,0,0]).reshape(4,1)
c=solve(a,b)

print(c)