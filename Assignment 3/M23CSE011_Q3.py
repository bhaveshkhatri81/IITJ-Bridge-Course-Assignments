def longest_consecutive_subsequence(arr):
    if not arr:
        return 0
    
    arr_set = set(arr)
    longest_length = 0
    
    for num in arr_set:
        if num - 1 not in arr_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in arr_set:
                current_num += 1
                current_length += 1
            
            longest_length = max(longest_length, current_length)
    
    return longest_length

input_str = input()
arr = list(map(int, input_str.split()))

result = longest_consecutive_subsequence(arr)
print(result)

