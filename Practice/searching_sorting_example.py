# Write a program in Python to implement Binary Search. Implement both iterative and recursive versions.

# Iterative Binary Search
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Recursive Binary Search
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


# Example usage
arr = [10, 20, 30, 40, 50, 60, 70]
target = 40

# Iterative
result1 = binary_search_iterative(arr, target)
print("Iterative: Element found at index", result1 if result1 != -1 else "Not found")

# Recursive
result2 = binary_search_recursive(arr, 0, len(arr) - 1, target)
print("Recursive: Element found at index", result2 if result2 != -1 else "Not found")