import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Define pivot within the function scope

    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(lesser) + equal + quicksort(greater)


def median_of_three(a, b, c):
    return sorted([a, b, c])[1]


arr = [12, 4, 5, 6, 7, 3, 1, 15]

pivot = arr[0]
result_a = quicksort(arr.copy())

pivot = arr[len(arr) // 2]
result_b = quicksort(arr.copy())

pivot = random.choice(arr)
result_c = quicksort(arr.copy())

pivot = median_of_three(arr[0], arr[len(arr) // 2], arr[-1])
result_d = quicksort(arr.copy())

pivot = median_of_three(arr[0], arr[1], arr[2])
result_e = quicksort(arr.copy())

print("Option A:", result_a)
print("Option B:", result_b)
print("Option C:", result_c)
print("Option D:", result_d)
print("Option E:", result_e)
