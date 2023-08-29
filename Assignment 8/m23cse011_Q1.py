def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1  

    
    dp = [[0] * n for _ in range(n)]

    
    split_points = [[0] * n for _ in range(n)]

    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')  
            for k in range(i, j):
                
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split_points[i][j] = k

    
    def construct_order(i, j):
        if i == j:
            return chr(65 + i)  
        split = split_points[i][j]
        return "(" + construct_order(i, split) + construct_order(split + 1, j) + ")"

    
    min_scalar_operations = dp[0][n - 1]
    order_of_operations = construct_order(0, n - 1)

    return min_scalar_operations, order_of_operations


dimensions = [5, 10, 8, 5]


min_operations, order = matrix_chain_multiplication(dimensions)


print("Minimum scalar operations:", min_operations)
print("Order of operations:", order)
