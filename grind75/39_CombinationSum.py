"""
thinking:
    
    my guess is brute force will TLE.... but maybe not because candidates is only 30 elements
    
    since we can build intermediate sums (e.g. 3x candidate[0] is a known quantity)
        I would think that we can use DP
        can also lean on backtracking because we can avoid trying combos that will certainly exceed target
    
aproach:
    
    brute force:
        not worth trying
    
    recursive backtracking:
        recursively perform DFS on an n-ary tree constructed from candidates
        backtrack when the running sum exceeds target
    
    dynamic programming:
        approach #3 here https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
    
"""

# from the forum
# dynamic programming
# T: O(n * t^2) where n is size of candidates and t is target
# S: O(t^2) where t is target
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(c, target+1):
                if i == c: 
                    dp[i].append([c])
                for combo in dp[i-c]:
                    dp[i].append(combo + [c])
            print(dp)
        return dp[-1]

# recursive backtracking
# T: O() 
# S: O(a) where a is the number of possible combinations explored (but not those cut short by backtracking)
class __Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursive helper, returns nothing but appends to 
        def recurse(candidates: List[int], start: int, target: int, runningCombo: List[int], runningSum: int, combos: List[List[int]]) -> None:
            # base cases
            if runningSum > target:
                return # backtrack
            elif runningSum == target:
                combos.append(runningCombo)
                return
            # recursion
            for i in range(start, len(candidates)):
                c = candidates[i]
                recurse(candidates, i, target, runningCombo + [c], runningSum+c, combos)
            return # if start == len(candidates)                    
        
        # initialize list of combinations
        combos = []
        recurse(candidates, 0, target, [], 0, combos) 
        return combos
            
            
            
            
            
            
            
            
            
            
            
            
        
