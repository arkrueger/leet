"""
approach:
    easy/cheat:
        put nums into a deque, pop the deque into nums' first k positions (reversed) 
        popleft for the remaining positions in num (not reversed)
        return nums
    
    edit in place:
        using a swap var
        determine which positions will get swapped based on k
        swap them
            the challenge is that position a doesn't swap for position b
            instead, position a -> position b, but position b -> position c
            so we should loop n times: start with index i = 0
                move nums[i] to index i+k (after storing nums[i+k] in swap)
                increment i by k
                voila
    brute force:
        helper function to rotate list by 1
        call the array k times
"""
# brute force
# gets TLE on large test cases but passes most
# T: O(n*k)
# S: O(1)
class __Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        if k > size:
            k = k % size # all k > len(nums) are degenerate
        if k == 0 or not nums: # must come after the k adjustment
            return
        for i in range(k):
            self.rotateOnce(nums)
        return None
    
    def rotateOnce(self, nums: List[int]) -> None:
        swap = nums[-1]
        for i, v in enumerate(nums):
            nums[i], swap = swap, nums[i]
        return None
        
        
        
# "Cyclic Replacements" - official leetcode solution with improvements for readability
# T: O(n)
# S: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k % size # adjust k if it's more than one full rotation
        if size == 1 or k == 0: # no point in rotating
            return            
        start = 0 # we use this to mark the index we started at so we don't repeat a replacement action
        i, swap = start, nums[start]
        for loop in nums:#while count < size: # we won't use loop var
            nxt = (i+k) % size # "wrap" the index back around if out of bounds
            nums[nxt], swap = swap, nums[nxt] # drop cargo and load up
            i = nxt
            if start == i:
                start += 1
                i, swap = start, nums[start]
                
            


# easiest way with zero thought
# T: O(n+k) (n for the creation of deque, k for rotation)
# S: O(n)
class __Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k >= len(nums):
            k = k % len(nums)
        from collections import deque
        q = deque(nums)
        for i in reversed(range(k)):
            nums[i] = q.pop()
        for i in range(k,len(nums)):
            nums[i] = q.popleft()
        return
        
