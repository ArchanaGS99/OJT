import numpy as np
arr = np.array([1, 2, 3, 2, 1, 4, 3, 2, 5])
unique_values, indices = np.unique(arr, return_inverse=True)
frequency = np.bincount(indices)
print("Unique Values:")
print(unique_values)
print("Frequency:")
print(frequency)