"""
approach:
    
    binary search: (two passes)
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
        
    modified binary search: (single-pass)
    ****I misunderstood some aspects of the indexing relative to the seam while writing this****
    ****leaving it up so I can come back and read it, but it's wrong as it's currently written****
        it's actually even easier to to a single binary search
        except that we change the comparisons made inside the loop
        while left <= right:
            make mid as normal (left+right)/2
            check for target (nums[mid] == target) -> if so, return mid
            if nums[left] < nums[mid], then we know that left and mid are on the same side relative to the "seam"
                now we want to check if target is between left and mid, i.e. nums[left] <= target <= nums[mid]
                    -> if so, shift towards the left, so set right = mid - 1
                    to clarify, this means left and mid are entirely contained in the ascending region before the seam (if nums and left spanned the seam, then nums[mid] would be less than nums[left]) or entirely contained in the ascending region after the seam
                    -> if not, then target is in the region on the other side of the seam,
                        so we want to shift rightwards, set left = mid + 1
            else (i.e. nums[left] > nums[mid])
                then we know that mid is after the "seam"
                now we want to check if target is between mid and right
                i.e. is nums[mid] <= target <= nums[right]
                    -> if so, shift rightwards, set right = mid - 1
                    -> if not, shift leftwards, set left = mid + 1
        in other words
        if (mid is before the seam and target is between left and mid) or (mid is after the seam and target is not between mid and right):
            shift leftwards (set right = mid - 1)
        else, i.e. (mid is after the seam and target is between mid and right) or (mid is before the seam and target is not between left and mid):
            shift rightwards (set left = mid + 1)
                
                
    
"""

# modified binary search
# T: O(logn)
# S: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            print("left: ", left, " right: ", right, " mid: ", mid)
            # check for exit case
            if nums[mid] == target: ans = mid
            # readable conditionals
            midLeftSameRegion = nums[left] <= nums[mid] # if left and mid are on the same side of the seam
            targetBtnLeftMid = nums[left] <= target <= nums[mid] # if target is between left and mid
            targetBtnMidRight = nums[mid] <= target <= nums[right] # if target is between mid and right
            
            if (midLeftSameRegion and targetBtnLeftMid) or (not midLeftSameRegion and not targetBtnMidRight):
                right = mid - 1
            else:
                left = mid + 1
        return ans


# 2x binary search
# T: O(logn)
# S: O(1)
class __Solution:
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

    
    
    

