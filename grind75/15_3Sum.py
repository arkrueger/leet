"""
approach:
    hashy brute force:
        recalling the hash map solution from Two Sum, we can employ it in a 3 Sum solution
        for each element of the array, set the new "target" to target - element
            call the Two Sum solution to find the two elements that sum to target (excluding the original element)
            -> our triplet becomes (element, TwoSum[0], TwoSum[1])
        how to avoid duplicate triplets?
            1) could remove any duplicates from the result after building it
            2) could check if answer is a duplicate before appending it to the result
            3) avoid iterating over the elements that we already examined
    
    dynamic programming?
        in the "hashy brute force" solution above, there are a lot of repeated function calls
            -> wait, there are a lot of repeated examined elements (i.e. examining i and j)
                but the pivots are different...
    
    sorted array?
        sort the array - this is easier than TwoSum because we return the numbers, not the indices
             so we don't need to track the indices
             sidebar - we can only have 1 zero or 3 zeros in any answer set, never 2 zeros
        start from the outside indices...
        checking the forum

also see:
https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
https://leetcode.com/problems/3sum/discuss/7384/My-Python-solution-based-on-2-sum-200-ms-beat-93.37
            
        
"""

# sorted array - recreated from forum
# T: O()
# S: O()
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2): # last i element is 3rd from end so that we can form a triplet
            if i > 0 and nums[i] == nums[i-1]: # don't use the same starting element more than once
                continue
            l, r = i+1, len(nums)-1 # start left pointer after i, start right index at end
            while l < r: # we will increase/decrease these as necessary but they can't cross
                s = nums[i] + nums[l] + nums[r]
                # now perform the classic iterative TwoSum dance, holding i constant
                if s < 0: # walk the left side up
                    l += 1
                if s > 0: # walk the right side down
                    r -= 1
                if s == 0: # append and select a new l and r
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # move the l cursor to the end of repeats, if applicable
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # move the r cursor to the end of repeats, if applicable
                        r -= 1
                    l += 1 # move l past the repeat region (if it existed) to a new number
                    r -= 1 # same for r cursor
        return res       
    

# hashy brute force
# gets TLE, but passes 317/318 cases - it works but it's slow
# T: O(n^2) 
# S: O(n)
class __Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums must be at least 3 long
        if len(nums) < 3:
            return []
        # vars
        res = set()
        # fix each element and find its complements 
        for i, c in enumerate(nums):
            temp = self.twoSum(nums, c, 0, i)
            if temp:
                res = res.union(temp)
        
        # convert res back to a list of lists
        res = [list(e) for e in list(res)]
        
        return res
    
    # helper function to find the two sum portion
    def twoSum(self, nums: List[int], pivot: int, target: int, pivotIndex: int) -> List[List[int]]:
        target = target - pivot # we want to find sets of two that sum to 
        comps = {} # complements
        res = set() # store solutions in res (using a set will prevent duplicates)
        for i, c in enumerate(nums):
            if i == pivotIndex: # skip the pivot element
                continue
            # check if current element is the complement to an already-traversed element
            if c in comps:
                res.add(tuple(sorted([pivot, c, comps[c]])))
            comps[target-c] = c
        return res
    
    