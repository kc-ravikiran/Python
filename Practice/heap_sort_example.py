# Write a program in Python to implement Heap Sort.

def heapify(arr, n, i):
    largest = i        # Assume root is largest
    left = 2 * i + 1   # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap current root with last element
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify reduced heap
        heapify(arr, i, 0)


# Example usage
arr = [63, 29, 18, 22, 117, 13, 18]
heap_sort(arr)

print("Sorted array:", arr)
