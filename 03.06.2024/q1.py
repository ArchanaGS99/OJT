# count the number of non-zero values
import numpy as np
arr = np.array([1, 2, 0, 3, 0, 4, 5])
non_zero_count = np.count_nonzero(arr)
print("Number of non-zero values:", non_zero_count)