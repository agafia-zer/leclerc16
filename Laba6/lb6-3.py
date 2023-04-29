#Клоннирование данных и Объединение массивов

import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
B = A[::-1]
C = A[:, ::-1]

D = np.stack((A, B, C))
print(D.shape)



A = np.ones((2, 1, 2))
B = np.zeros((2, 3, 2))

C = np.concatenate((A, B), 1)
print(C.shape)



A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
B = A[::-1]
C = A[:, ::-1]

D = np.stack((A, B, C))
D[0, 0, 0] = 0
print(A)

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.repeat(A, 2))

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
B = np.repeat(A, 2).reshape(A.shape[0], A.shape[1], -1)
print(B)
