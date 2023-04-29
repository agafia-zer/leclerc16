import numpy as np


#Рассмотрим примеры со скалярами и векторами:

# скаляры
A = 2
B = 3

print(np.dot(A, B), '\n')

# вектор и скаляр
A = np.array([2., 3., 4.])
B = 3

print(np.dot(A, B), '\n')

# вектора
A = np.array([2., 3., 4.])
B = np.array([-2., 1., -1.])

print(np.dot(A, B), '\n')

# тензор и скаляр
A = np.array([[2., 3., 4.], [5., 6., 7.]])
B = 2

print(np.dot(A, B), '\n')


#С тензорами посмотрим только на то, как меняется размер геометрия результирующего массива:
# матрица (тензор 2) и вектор (тензор 1)
A = np.ones((5, 6))
B = np.ones(6)

print('A:', A.shape, '\nB:', B.shape, '\nresult:', np.dot(A, B).shape, '\n\n')

# матрицы (тензора 2)
A = np.ones((5, 6))
B = np.ones((6, 7))

print('A:', A.shape, '\nB:', B.shape, '\nresult:', np.dot(A, B).shape, '\n\n')

# многомерные тензора
A = np.ones((5, 6, 7, 8))
B = np.ones((1, 2, 3, 8, 4))

print('A:', A.shape, '\nB:', B.shape, '\nresult:', np.dot(A, B).shape, '\n\n')


#Для выполнения произведения тензоров с использованием других осей, вместо 
#определенных для dot можно воспользоваться tensordot с явным указанием осей:

A = np.ones((1, 3, 7, 4))
B = np.ones((5, 7, 6, 7, 8))

print('A:', A.shape, '\nB:', B.shape, '\nresult:', np.tensordot(A, B, [2, 1]).shape, '\n\n')