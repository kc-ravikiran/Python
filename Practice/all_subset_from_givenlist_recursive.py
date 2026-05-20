# Write a recursive Python function to generate all subsets of a given set.

def generate_subsets(arr):
    if not arr:
        return [[]]
    
    first = arr[0]
    
    # Generate subsets of remaining elements
    rest_subsets = generate_subsets(arr[1:])
    
    # Add first element to each subset
    with_first = []
    for subset in rest_subsets:
        with_first.append([first] + subset)
    
    # Combine subsets with and without first element
    return rest_subsets + with_first


# Example usage
data = [1, 2, 3, 4]
subsets = generate_subsets(data)

print(subsets)