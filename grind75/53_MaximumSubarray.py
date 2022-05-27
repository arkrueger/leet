### GRIND 75 SECOND PASS ###

"""
approach:
    running tally:
        loop along the array
            keep track of the current sum
            if larger than previous max, store in max
            if at any point the sum dips below 0, we may as well have started from the current index
                (because a negative sum isn't helpful)
                -> "sink" the cumulative by resetting sum to 0 if sum is negative
        return the maximum sum found
        -------note about currentSum = max(currentSum, 0):
                    it might seem like this will fail if all the values in the array are negative
                    but that's not true. consider [-2,-1,-3,-5]
                    as long as we start maxSum as nums[0] (i.e. -2) then we will still settle on -1 as the larger sum
                    preventing currentSum from dipping below zero only prevents us from making a negative value *more negative* -- we're still allowing the algorithm to reset and count fresh *less negative* values 
    
    divide and conquer:
        lemme see... 
        we want to split the array into two halves
            find the max sum in the symmetrical(?) subarray spanning the centerpoint (expanding left&right from center)
            find the max sum starting from the rightmost index in the right half (expanding leftward)
            find the max sum starting from the leftmost index in the left half (expanding rightward)
        
    
"""
# divide and conquer
# Gets TLE, but should work (run the C++ version to avoid TLE)
# T: O(?)
# S: O(?)
class Solution:
    def maxSubArray(self, nums: List[int], low: int=-99, high: int=-99) -> int:
        size = len(nums)
        low = 0 if low == -99 else low
        high = size - 1 if high == -99 else high
        mid = (low+high)//2
        
        if high <= low:
            return nums[low]
        
        # get left-radiating sum
        leftSum = self.getSum(nums[mid::-1]) # nums is reversed because left subarray starts at mid and grows 0-ward
        # get right-radiating sum
        rightSum = self.getSum(nums[mid+1:high+1]) 
        # get recursive sums
        recurseLeftSum  = self.maxSubArray(nums, low, mid)
        recurseRightSum = self.maxSubArray(nums, mid+1, high)
        # return overall max
        centerSum = leftSum + rightSum
        recursiveSum = max(recurseLeftSum, recurseRightSum)
        return max(centerSum, recursiveSum)
        
            
    # helper func to get max sum with fixed starting position
    def getSum(self, nums: List[int]) -> int:
        currentSum  = 0
        maxSum      = nums[0]
        for i in nums:
            currentSum += i
            maxSum = max(maxSum, currentSum)
        return maxSum
        
        
        


# running tally
# T: O(n)
# S: O(1)
class __Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for i in nums:
            currentSum += i
            maxSum = max(maxSum, currentSum)
            currentSum = max(currentSum, 0) # don't allow currentSum to drop below zero unless max is below zero
        return maxSum
    
    
    
    