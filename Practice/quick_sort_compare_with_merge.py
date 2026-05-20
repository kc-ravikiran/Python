# Write a program in Python to implement Quick Sort. Also, compare its performance with Merge Sort.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]   # Choose middle element as pivot

    # Divide array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)