"""
approach:
    
    recursive DFS with backtracking:
        treat candidates as an n-ary tree where no candidate can be its own descendant
            (b/c we can't repeat candidates in the combination)
        traverse this tree by recursive DFS
        backtracking: abandon any partial combinations that exceed target
    
"""

# from the forum
# dfs backtracking
# T: O(2^n) but not sure
# S: O(s + a) where s is recursive call stack and a is the output list
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates: List[int], target: int, start: int, runningCombo: List[int], combos: List[List[int]]) -> None:
            if target <= 0:
                if target == 0:
                    combos.append(runningCombo)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                c = candidates[i]
                dfs(candidates, target-c, i+1, runningCombo + [c], combos)
        
        combos = []
        candidates.sort()
        dfs(candidates, target, 0, [], combos)
        return combos
        



# from the solution
# backtracking with index
# T: O(2^n)
# S: O(n)
class __Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb: List[int], remaining: int, current: int, results: List[List[int]]) -> None:
            if remaining == 0:
                results.append(list(comb))
                return
            
            for next_current in range(current, len(candidates)):
                # don't repeat? not sure exactly
                if next_current > current and candidates[next_current] == candidates[next_current-1]:
                    continue # for any next_current after current (range starts at current), check if the candidate value is repeated (recall the candidate was sorted in the outer function). If it is, then jump to the next iteration (the next next_current)
                
                pick = candidates[next_current]
                if remaining - pick < 0: 
                    break # backtrack, don't pursue overshoots
                
                comb.append(pick)
                backtrack(comb, remaining - pick, next_current + 1, results)
                comb.pop()
        
        # main function
        candidates.sort()
        comb, results = [], []
        backtrack(comb, target, 0, results)
        return results
                
        
        
        

# recursive DFS with backtracking
# gets TLE
# T: O(?)
# S: O(?)
class __Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursive helper
        def dfs(candidates: List[int], start: int, remaining: int, runningCombo: List[int], combos: int) -> None:
            # base cases
            # print(target)
            if remaining == 0:
                combos.append(runningCombo)
                return
            if remaining < 0: # overshot, backtrack
                return
            # recurse
            for i in range(start+1, len(candidates)):
                c = candidates[i]
                # print(runningCombo, "   ", target, "    ", target-c)
                dfs(candidates, i, remaining-c, runningCombo+[c], combos)
        
        combos = []
        candidates = sorted(candidates)
        for i, c in enumerate(candidates):
            dfs(candidates, i, target-c, [c], combos)
        # get rid of duplicates
        uniqueCombos = set()
        for p in combos:
            uniqueCombos.add(tuple(sorted(p)))
        # print(uniqueCombos)
        # print(combos)
        return [list(x) for x in uniqueCombos]
