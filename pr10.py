import numpy as np

mat = np.array([[10, 20, 30], [40, 50, 60]])
print("Original matrix:\n", mat)

in_val = mat[1, 2]
print("\nElement at row 1, column 2:", in_val)

slic_matrix = mat[:, 1:3]
print("\nSub-matrix containing columns 1 and 2:\n", slic_matrix)

re_mat = mat.reshape(3, 2)
print("\nArray reshaped to 3x2:\n", re_mat)

b_result = mat + 15
print("\nMatrix after adding scalar 15:\n", b_result)

print("\nAddition by 5:\n", mat + 5)
print("\nElement-wise multiplication by 3:\n", mat * 3)
print("\nSquare of elements:\n", mat ** 2)