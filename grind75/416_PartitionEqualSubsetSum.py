"""
approach:
    
    iterative two pointer:
    !! Does not work for all cases, e.g. [1,1,2,2] can be split into [1,2],[1,2] but this method will say it cannot
        sort the array ascending
        pointers: left = 0, right = end
        temp var: balance = nums[right]
        while left < right:
            subtract nums[left] from balance
            if balance <= 0:
                right -= 1
                balance += nums[right]
        if balance = 0 when the loop is finished, return True
        otherwise False
        
    DP with memoization:
        ...?
        flag to review this later, looks like a lot of companies have been using this problem recently
        most DP solutions I can wrap my head around, but this one has me stumped
        
"""


# official leetcode solution
# dynamic programming, bottom up tabulation, 2D array
# T: O(m*n) because we iteratively fill the DP array
# S: O(m*n) for the DP array
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        fullSum = sum(nums)
        # if the full sum is odd, no solution is possible b/c we only allow integers
        if fullSum % 2 == 1:
            return False
        # setting up for dp
        halfSum = fullSum//2
        n = len(nums)
        dp = [[False] * (halfSum+1) for _ in range(n+1)] # (n+1) rows, (halfSum+1) cols
        dp[0][0] = True # need to seed a True
        # computation
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(halfSum+1):
                if j < curr: # j is a representation of a potential subset sum (between 0 and halfSum)
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[n][halfSum]
        
              

# fundamentally flawed
# two pointer
# T: O(n) 
# S: O(1)
class __Solution:
    def canPartition(self, nums: List[int]) -> bool:
        left, right = 0, len(nums)-1
        nums.sort()
        balance = nums[right]
        while left < right:
            balance -= nums[left]
            left += 1
            if balance <= 0 and right > left:
                right -= 1
                balance += nums[right]
        return True if balance == 0 else False
