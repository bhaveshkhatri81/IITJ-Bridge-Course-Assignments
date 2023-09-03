# Quick Sort Algorithm + Quick Sort with Randomized Pivot Selection Strategy.
# Comparing the value of of Quick Sort and Randomized QS



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)




import random

def random_qs(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return random_qs(left) + middle + random_qs(right)













import timeit


def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]



# execution time for standard Quicksort
def standard_quicksort_performance():
    arr = generate_random_list(1000)  
    return quicksort(arr)

# execution time for Quicksort with Random_QS
def randomized_quicksort_performance():
    arr = generate_random_list(1000)  
    return lambda: random_qs(arr)

# Compare 
standard_time = timeit.timeit(standard_quicksort_performance, number=1000)  
randomized_time = timeit.timeit(randomized_quicksort_performance, number=1000)  

print("Standard Quicksort Execution Time:", standard_time)
print("Randomized Quicksort Execution Time:", randomized_time)


arr = [1,4,2,5,3,6,3,8,3,6,8,3]


print(F"The Output with quick sort {quicksort(arr)}")
print("The output with randomized quick sort", random_qs(arr))
