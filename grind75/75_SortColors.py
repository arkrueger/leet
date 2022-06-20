"""
approach:
    
    iterative one pass analysis, one pass sort:
        technically 2 pass (one for counting, one for sorting)
        iterate over the array:
            count up red, white, and blue objects
        iterate over the array:
            if red count > 0:
                current element = red
                decrement red
            elif white count > 0:
                current element = white
                decrement white
            else:
                current element = blue
    
    true one-pass:
        have 3 pointers
            here
            endRed (what should come first)
            startBlue (what should come last)
        
"""

# one pass analysis, one pass sort
# T: O(n) specifically O(2n)
# S: O(1)
class __Solution:
    def sortColors(self, nums: List[int]) -> None:
        # count up the colors
        red = white = 0
        for v in nums:
            if v == 0:
                red += 1
            if v == 1:
                white += 1
        # change the elements in place
        for i, _ in enumerate(nums):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
        # fin
    
    
# true one-pass
# T: O(n) 
# S: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # pointers for current, and just outside of red boundary, just inside of blue boundary
        here = 0
        endRed = 0
        startBlue = len(nums) - 1
        # iterate
        while here <= startBlue:
            if nums[here] == 0: # then move it to the end of the reds
                nums[here], nums[endRed] = nums[endRed], nums[here]
                endRed += 1
                here += 1
            elif nums[here] == 2: # then move it to the front of the blues
                nums[here], nums[startBlue] = nums[startBlue], nums[here]
                startBlue -= 1
                # don't move the here pointer because we need to analyze what we swapped in
            else: # nums[here] == 1
                here += 1
        # fin
