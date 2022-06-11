"""
approach:
    
    recursive DFS with backtracking:
        treat the combination like a tree, recurse within inner loop
        avoid duplicate pairs by starting inner loop (i.e. the loop in the ensuing recursive call)
            at the current index + 1
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # recursive helper function
        def dfs(n: int, c: int, k: int, runningCombo: List[int], ans: List[List[int]]) -> None:
            # base case
            if k == 0:
                ans.append(runningCombo)
                return
            # recursion
            for i in range(c, n+1):
                dfs(n, i+1, k-1, runningCombo+[i], ans)
        
        ans = []
        dfs(n, 1, k, [], ans)
        return ans
