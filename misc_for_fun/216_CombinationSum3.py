"""
approach:
    
    recursive DFS with backtracking:
        treat the possible combinations like a k-ary tree
        perform recursive DFS on the tree, ensuring no repeats per the problem statement
            recurse on the next index, k - 1, n - i
        base cases are when k == 0 -> if also n == 0, then we have a match
                                    -> else, we don't have a match, return
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(k: int, n: int, start: int, runningCombo: List[int], combos: List[List[int]]) -> None:
            # base cases
            if n <= 0 or k == 0:
                if n == 0 and k == 0:
                    combos.append(runningCombo)
                return
            # recursion
            for c in range(start, 10):
                dfs(k-1, n-c, c+1, runningCombo+[c], combos)
            return
            
        
        combos = []
        dfs(k, n, 1, [], combos)
        return combos
