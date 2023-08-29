
def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def convert_min_heap_to_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)


min_heap = [3, 5, 9, 15, 6, 8, 20, 10, 12, 18, 9]

print("Original minHeap:", min_heap)
convert_min_heap_to_max_heap(min_heap)
print("Converted maxHeap:", min_heap)
