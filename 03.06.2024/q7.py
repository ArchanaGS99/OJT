import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
# Perform matrix multiplication using the @ operator
result = matrix1 @ matrix2
# Perform matrix multiplication using the numpy.dot() function
result2 = np.dot(matrix1, matrix2)
print(result)
print(result2)