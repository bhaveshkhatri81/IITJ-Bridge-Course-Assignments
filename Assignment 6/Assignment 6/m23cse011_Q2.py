def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 4, 5, 6, 7, 3, 1, 15]

heap = []
for num in arr:
    heap.append(num)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

sorted_result_a = []
for _ in range(len(heap)):
    heap[0], heap[-1] = heap[-1], heap[0]
    sorted_result_a.insert(0, heap.pop())
    heapify(heap, len(heap), 0)

heapsort(arr)

print("Option A (Using Heap Operations):", sorted_result_a)
print("Option B (Directly Sorting):", arr)
