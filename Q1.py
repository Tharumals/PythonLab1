import numpy as np
import matplotlib

arr = np.ones([5, 5])

def identity_list(row, col):
    return np.identity(row)

def multiply_matrix(mat1, mat2):
    return np.matmul(mat1,mat2)


print(arr)
print(identity_list(5,5))
mat1 = np.array([1,2,3])
mat2 = np.array([10,20,30])

print(multiply_matrix(mat1,mat2))
