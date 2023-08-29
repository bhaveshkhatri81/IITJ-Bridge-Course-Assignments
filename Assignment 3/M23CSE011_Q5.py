def has_pair_with_sum(arr, x):
    seen = set()

    for num in arr:
        complement = x - num
        if complement in seen:
            return True
        seen.add(num)

    return False

arr = [1, 2, 3, 4, 5]
x = 9

result = has_pair_with_sum(arr, x)
print(result)

