# Import the numpy library
import numpy as np

# Create a 1D NumPy array
array_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(array_1d)

# Perform basic operations on the array
print("\nBasic Operations:")
print(f"Sum of elements: {np.sum(array_1d)}")
print(f"Mean of elements: {np.mean(array_1d)}")
print(f"Max element: {np.max(array_1d)}")
print(f"Min element: {np.min(array_1d)}")

# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(array_2d)

# Perform matrix operations
print("\nMatrix Operations:")
print("Transpose of the matrix:")
print(array_2d.T)

# Perform element-wise addition
array_add = array_2d + 10
print("\nElement-wise addition (add 10 to each element):")
print(array_add)

# Perform matrix multiplication
array_mul = np.dot(array_2d, array_2d)
print("\nMatrix Multiplication:")
print(array_mul)
