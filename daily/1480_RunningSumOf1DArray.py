class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # no restriction on editing nums, so just going to edit in place
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
