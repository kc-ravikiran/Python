# Write a program in Python to add two polynomials.
def add_polynomials(poly1, poly2):
    # Result polynomial
    result = []

    # Find the maximum length
    max_len = max(len(poly1), len(poly2))

    # Add coefficients
    for i in range(max_len):
        coeff1 = poly1[i] if i < len(poly1) else 0
        coeff2 = poly2[i] if i < len(poly2) else 0
        result.append(coeff1 + coeff2)

    return result


# Example usage
# Represent polynomial as list: [constant, x¹, x², x³, ...]
poly1 = [5, 0, 10, 6]   # 5 + 0x + 10x² + 6x³
poly2 = [1, 2, 4]       # 1 + 2x + 4x²

result = add_polynomials(poly1, poly2)

print("Resultant polynomial coefficients:", result)