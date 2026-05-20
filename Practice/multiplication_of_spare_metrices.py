# Write a program in Python to perform multiplication of two sparse matrices.

def multiply_sparse_matrices(mat1, mat2):
    result = {}

    # Iterate through elements of first matrix
    for (i, k1), v1 in mat1.items():
        # Match with second matrix
        for (k2, j), v2 in mat2.items():
            if k1 == k2:  # Column of mat1 == row of mat2
                if (i, j) not in result:
                    result[(i, j)] = 0
                result[(i, j)] += v1 * v2

    return result


# Example usage
# Format: (row, col): value
matrix1 = {
    (0, 1): 5,
    (1, 2): 8
}

matrix2 = {
    (1, 0): 3,
    (2, 1): 6
}

result = multiply_sparse_matrices(matrix1, matrix2)

print("Resultant Sparse Matrix:")
for key, value in result.items():
    print(f"Position {key} -> {value}")