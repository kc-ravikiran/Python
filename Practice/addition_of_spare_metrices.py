# Write a program in Pythonfor addition of two sparse matrices.
def add_sparse_matrices(mat1, mat2):
    result = {}

    # Add elements from first matrix
    for key in mat1:
        result[key] = mat1[key]

    # Add elements from second matrix
    for key in mat2:
        if key in result:
            result[key] += mat2[key]
        else:
            result[key] = mat2[key]

    # Remove zero values (if any)
    result = {k: v for k, v in result.items() if v != 0}

    return result


# Example usage
# Format: (row, col): value
matrix1 = {(0, 1): 5, (1, 2): 8}
matrix2 = {(0, 1): 3, (2, 0): 6}

result = add_sparse_matrices(matrix1, matrix2)

print("Resultant Sparse Matrix:")
for key, value in result.items():
    print(f"Position {key} -> {value}")
