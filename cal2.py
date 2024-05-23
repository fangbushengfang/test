import math

import numpy as np

a = np.array([1, 2, 3, 4, 5]).reshape(1, 5)
a1 = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5]).reshape(1, 6)
h = math.pi / 36
b = a * h
b1 = a1 * h
c = (4 - np.power(np.sin(b), 2)) ** 0.5
c1 = (4 - np.power(np.sin(b1), 2)) ** 0.5

answer = 0.5 * h * (2 + (15 / 4) ** 0.5 + 2 * np.sum(c))
answer_simpson = 1 / 6 * h * (2 + (15 / 4) ** 0.5) + 2 / 3 * h * (np.sum(c1))+1/3*h*(np.sum(c))

print(answer)
print(answer_simpson)
