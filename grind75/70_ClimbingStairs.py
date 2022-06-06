"""
approach:
    build the solution from the bottom up:
        that is, let's say our n = 5
        how ways can I get to:
            step        ways    step pattern
            1           1       1
            2           2       1 1 / 2
            3           3       1 1 1 / 1 2 / 2 1
            4           5       1 1 1 1 / 2 2 / 1 1 2 / 2 1 1 / 1 2 1 / 
            5           8       1 1 1 1 1 / 2 1 1 1 / 1 2 1 1 / 1 1 2 1 / 1 1 1 2 / 2 2 1 / 2 1 2 / 1 2 2
            pattern is ans[i] = ans[i-1] + ans[i-2]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0] * (n+1) # need a placeholder for 0 because we use i-2 later
        ans[0] = ans[1] = 1 # only 1 way to get to 0 (stay put) and 1 is trivial
        for i in range(2, n+1): # start at 2 b/c 0 and 1 are already populated
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]
