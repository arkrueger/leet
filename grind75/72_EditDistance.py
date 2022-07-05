# doing this after seeing it in a Pramp interview

# dynamic programming, bottom-up
# T: O(mn) to iterate over the dp matrix
# S: O(mn) to hold the dp matrix
class __Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # if one or both strings are empty
        if m*n == 0:
            return m+n
        # dp array
        dp = [ [0] * (n+1) for _ in range(m+1)] # plus 1 because we need to store row/col for empty string
        # initialize top and left edges
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        # compute
        for i in range(1, m+1): # start at 1 because left col is already init
            for j in range(1, n+1): # same b/c top row is already init
                above = dp[i-1][j] + 1 # if we came from above
                left = dp[i][j-1] + 1 # if we came from the left
                uld = dp[i-1][j-1] # if we came from the diagonal up left
                if word1[i-1] != word2[j-1]:  # if we're comparing unequal characters, account for a replacement operation
                    uld += 1
                dp[i][j] = min(above, left, uld)
        # end
        return dp[m][n] # bottommost leftmost index

# dp with top down approach
# T: O(m*n?)
# S: O(m*n?)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            m, n = len(word1), len(word2)
            # base cases
            if i == m and j == n:   return 0;
            if j == n and i < m:    return m - i;
            if i == m and j < n:    return n - j;
            # recursion
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            else:
                above = dp(i+1, j)
                left = dp(i, j+1)
                uld = dp(i+1, j+1)
                return 1 + min(above, left, uld)
        # main
        return dp(0,0)
