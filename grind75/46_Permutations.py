"""
approach:
    
    recursive dfs:
        treat the permutations as an n-ary tree
        recursively perform dfs on the input array
        
"""


# recursive dfs
# T: O(2^n) from dfs n-ary tree traversal, where n is the length of the input list
# S: O() not sure
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], runningPermutation: List[int], permutations: List[List[int]]) -> None:
                # base cases
                if len(runningPermutation) == len(nums):
                    permutations.append(runningPermutation)
                    return
                # recursion
                for c in nums:
                    if c not in runningPermutation:
                        dfs(nums, runningPermutation+[c], permutations)
        
        permutations = []
        dfs(nums, [], permutations)
        return permutations
