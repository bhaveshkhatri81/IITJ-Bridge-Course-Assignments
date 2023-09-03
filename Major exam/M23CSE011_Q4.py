def longest_common_subsequence(S1, S2):
    
    m, n = len(S1), len(S2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs.append(S1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    
    lcs.reverse()
    return lcs, len(lcs)

# Example usage
S1 = [0, 3, 6, 9, 12]
S2 = [0, 1, 1, 2, 3, 5, 8, 13, 21]
result, length = longest_common_subsequence(S1, S2)
print(f"The longest common subsequence is {result}, and its length is {length}.")
