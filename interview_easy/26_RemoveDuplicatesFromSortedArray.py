"""
approach:
    iterative / two pointers
        iterate over the array
        two pointers - one at current read and another at current write
        if current read == previous write, do nothing
        else if current read > previous write:
            write current read to current write
            move write pointer forward
            move read pointer forward
    
    alternative two pointer
        found in the forum
        this is more compact and straightforward than my solution
        basically, 
            keep track of our write index, starting from zero
            scan the list for places where the next number is not equal to the current number
                set the element at the write index equal to the next number
                increment the write index
    
    easy - use a set (does this violate the O(1) space rule?)
        cast nums to a set
        k = size of set
        iterate over set and modify the first k of nums
        return k
"""
# alternative two pointer
# T: O(n) 
# S: O(1) 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 0
        for i, c in enumerate(nums[:-1]):
            if c < nums[i+1]:
                nums[k] = nums[i+1]
                k += 1
        return k


# convenience approach
# T: O(u) where u is the number of unique integers in nums
# S: O(u) 
class __Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        k = len(unique)
        for i, c in enumerate(unique):
            nums[i] = c
        return k

# iterative two pointer
# T: O(n)
# S: O(1)
class __Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if 1 == len(nums):
            return 1
        if 2 == len(nums):
            return 1 if nums[0] == nums[1] else 2
        k = 1 # the length of the subarray of interest
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] < nums[right]:
                left += 1
                nums[left] = nums[right]
                right += 1
                k += 1
            else:
                right += 1
        return k
    
    
    
    
