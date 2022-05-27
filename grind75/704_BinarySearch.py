### GRIND 75 SECOND PASS ###
"""
approach:
    binary search:
        set left and right as 0 and len-1 index
        find the middle
        compare the middle to the target
            if equal, return middle index
            if target is greater, store middle index in left
            if target is smaller, store middle index in right
            repeat until left == right
    
    bisect (convenience function):
        from the forum.
        use bisect to determine at which index target would need to be inserted to maintain sorted order
        if the index is within the bounds of the existing list (i.e. target is not > or < the entire list)
            then return the index only if nums[index] is equal to the target
            otherwise, return -1 because the target does not exist in the list
"""
# bisect (convenience function)
# T: O(logn) assuming that bisect implements a binary search
# S: O(1)
class Solution:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1

# binary search
# T: O(logn)
# S: O(1)
class __Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return -1