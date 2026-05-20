# Write a program in Python to implement Insertion Sort.
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]          # Element to be inserted
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key      # Place key at correct position

    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = insertion_sort(arr)

print("Sorted array:", sorted_arr)