import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag_sum = np.sum(np.diagonal(matrix))
print("Sum of diagonal elements in 3x3 matrix:", diag_sum)