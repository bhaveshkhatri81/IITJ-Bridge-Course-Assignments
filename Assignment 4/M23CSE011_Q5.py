
import heapq


def merge_k_sorted_arrays(arrays):
    heap = []  # Min-heap to store elements and their respective array index
    result = []

    for i in range(len(arrays)):
        if arrays[i]:  # Check if the array is not empty
            heapq.heappush(heap, (arrays[i][0], i, 0))

    while heap:
        val, arr_idx, idx = heapq.heappop(heap)
        result.append(val)

        if idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][idx + 1], arr_idx, idx + 1))

    return result


array1 = [2, 6, 9]
array2 = [1, 4, 7]
array3 = [3, 5, 8]

arrays = [array1, array2, array3]

merged_sorted = merge_k_sorted_arrays(arrays)
print("Merged and sorted array:", merged_sorted)
