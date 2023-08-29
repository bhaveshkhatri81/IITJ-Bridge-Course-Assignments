def longest_common_subsequence(strs):
    
    if len(strs) < 2:
        return 0, ""

    
    m = len(strs[0])
    n = len(strs[1])
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if strs[0][i - 1] == strs[1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    i, j = m, n
    lcs_length = dp[m][n]
    lcs_string = ""
    while i > 0 and j > 0:
        if strs[0][i - 1] == strs[1][j - 1]:
            lcs_string = strs[0][i - 1] + lcs_string
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, lcs_string


n = int(input("Enter the number of strings: "))
strs = []
for i in range(n):
    str_i = input(f"Enter string {i + 1}: ")
    strs.append(str_i)

lcs_length, lcs_string = longest_common_subsequence(strs)
print(f"The length of LCS is {lcs_length}, and the string is {lcs_string}.")
