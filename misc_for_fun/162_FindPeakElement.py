"""
Notes:
    Problem statement asks for T: O(logn) -> linear search is out, try binary search
    clarification on: "nums[-1] = nums[n] = -inf"
        a bit confusing since some languages use [-1] to indicate [n], but it's actually saying that on either side of the array, we can assume -inf
    we also have "nums[i] != nums[i+1]" i.e. no repeated numbers in a row -> no plateaus
    all together, we can conclude that we're guaranteed a peak
    even if the array is completely descending or completely ascending, having -inf on either side would give:
        ascending:      -inf 0 1 2 3 4 -inf -> 4 is our peak at index 4
        descending:     -inf 4 3 2 1 0 -inf -> 4 is our peak at index 0

approach:
    
    binary search:
        since we know there must be a peak somewhere inside the array
        we can analyze nums[i] and nums[i+1] to get insight on where we are relative to a peak
            possibility 1: nums[i] > nums[i+1]  -> we are past the peak
            possibility 2: nums[i] < nums[i+1]  -> we are before the peak
        just as in a plain binary search, we adjust our left and right cursors accordingly:
            mid is before peak -> move left to mid
            mid is after peak -> move right to mid
        
    note on binary search
        while right >= left
            mid is calculated with floor divide
            right is set to mid
            left is set to mid + 1
        other combos won't converge
        
"""

# binary search
# T: O(logn) binary search (divide search region by 2 each cycle)
# S: O(1) no new data structures allocated
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 1, len(nums) # shifted right because we will prepend -inf to nums before processing
        # bookend nums with -inf
        nums = [-inf] + nums + [-inf]
        # binary search
        while right >= left: # TODO check
            mid = (left + right) // 2
            # check if we are at a peak
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]: # found the peak
                return mid - 1
            if nums[mid] > nums[mid+1]: # descending -> we are past a peak, move right to mid
                right = mid
            elif nums[mid] < nums[mid+1]: # ascending -> we are before a peak, move left to mid
                left = mid + 1
                
                
                
                
                
            
