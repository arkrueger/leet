"""
approach:
    
    2x binary search:
        first pass to find the rotation (k)
            note: all values of nums are unique
            straightforward, the target i will be defined by nums[i] < nums[i-1]
            note: when comparing nums[mid] to understand if we shift left or right, 
                nums[0] is our comparison 
                because anything after the "seam" (that connects the end to the start) is guaranteed 
                to be lower than nums[0] 
                -> if nums[mid] > nums[0], we are before the seam
                -> if nums[mid] < 0, we are past the seam
        second pass to find the target
    
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first pass, find the rotation (searching for nums[i] < nums[i-1])
        n = len(nums)
        left, right = 1, n-1 # start left at index 1 because we need to use [i-1]
        # check the trivial case where the array is not rotated
        if nums[0] < nums[-1] or len(nums) == 1:
            k = 0
        else: # the array is rotated at an unknown pivot index k, so find k
            counter = 0
            while right >= left:
                mid = (left + right) // 2
                # check for target, and if not, compare with nums[0] 
                if nums[mid] < nums[mid-1]:
                    k = mid
                    break
                elif nums[mid] > nums[0]: # mid is before the "seam"
                    left = mid + 1
                else: # then nums[mid] < nums[0], which means mid is past the seam
                    right = mid - 1
        
        # now that we have k, we can perform an ordinary binary search but offset by k
        left, right = 0, n-1
        res = -1 # if we don't find the element in the list
        while right >= left:
            mid = (left + right) // 2
            sMid = (mid+k)%n if mid+k > 0 else 0 # shifted mid by k
            if nums[sMid] == target:
                res = sMid
                break
            elif nums[sMid] > target:
                right = mid - 1
            else: # then nums[sMid] < target
                left = mid + 1
            
        return res

    
    
    

