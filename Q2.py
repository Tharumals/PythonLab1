import numpy as np
import matplotlib
import math

zeros = np.zeros([10,10])

print(zeros)
#other functions similar to np.zeros are np.ones(),np.identity()

matrix1 = [1,3,4,5]
matrix2 = [6,7,8,9]

m1 = np.array(matrix1)
m2 = np.array(matrix2)

multiplication = np.dot(m1,m2)
print(multiplication)

addition = m1+m2
subtraction = m1-m2
print(addition)
print(subtraction)

w = np.array([4,7,9,-1,3,5,8])

max = np.max(w)
min = np.min(w)
sum = np.sum(w)

print('Max: ',max )
print('Min: ',min )
print('Total: ',sum )

minimumElement = np.amin(w)
print('Minimum Element: ',minimumElement)

A = np.arange(start=5, stop=23, step=2)
B = A.reshape(3,3)

Cosine_of_A = np.cos(A)
print('Cosine_of_A',Cosine_of_A)

exponential = np.exp(A)
print('exponential_of_A',np.exp(A))

for i in range(len(A)):
    if i in range(2:6):
        print(A[i])

#display column values
print(B[:,0])

#creating arrays with random numbers
rand_array1 = np.random.randint(10,90,(4,4))
rand_array2 = np.random.randint(34,76,(4,4))

vertical_stack = np.vstack((rand_array1,rand_array2[:,-1]))
c = np.hstack(vertical_stack,rand_array2[:,None]))

print('stacked arrays: ',c)

c_horizontal_split = np.hsplit(c, 4)
c_vertical_split = np.vsplit(c, 4)

