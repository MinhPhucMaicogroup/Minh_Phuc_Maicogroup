import numpy as np
from math import sqrt
from math import floor
from numpy.lib.twodim_base import diag

def mat_mul(A, B):
    return A.dot(B)


def even_mat(A):
    B = np.zeros(A.shape, dtype="int16")
    B[A%2 == 0] += 1
    return B


def check_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for i in range(2, floor(sqrt(number))+1):
        if number%i == 0:
            return False
    return True


A = np.random.randint(0, 100, (3, 4))
B = np.random.randint(0, 100, (4, 4))
print("a)")
print("Matrix 3x4:")
print(A)
print("Matrix 4x4:")
print(B)
print("Matrix AxB:")
print(mat_mul(A, B))
print("")

A = np.random.randint(0, 100, (4, 4))
print("b)")
print("Random matrix 4x4:")
print(A)
print("Even Matrix:")
print(even_mat(A))
print("")

A = np.random.randint(0, 100, (5, 5))
print("c)")
print("Random 5x5 Matrix: ")
print(A)
print("After rotate left:")
A = np.roll(A, -1)
print(A)
diagonal = np.diag(A)
print("Diagonal array:")
print(diagonal)
vectorize = np.vectorize(check_prime)
result = vectorize(diagonal)
print("Number of Prime Numbers:", np.count_nonzero(result))


