### GRIND 75 SECOND PASS ###
"""
approach:
    brute force:
        try each element added with each other element
            possible to index i, j = i+1 to only get below the diagonal on the matrix and be a bit more efficient
        return when we see a solution cause we know there's only one solution
    
    hash map:
        loop through the list, store the additive complement of each element in a dict (complement is the key, index is the val)
        check if the current nums val is already recorded as a complement
            if so, return the current index and the index indicated by the complement
    
    sorted array:
        sort the array & keep track of their original indices (e.g. convert to a list of tuples)
        start from the large side of the array 
        take this number as the anchor, call it "larger"
        (you might be tempted to take "larger" as the next smallest value below anchor, but this doesn't work with negatives in list)
        outer loop: 
            inner loop:
                starting from the smallest number and continuing to just below larger, add it to the larger and compare to target
                return if the sum == target
                break if sum > target
            once the inner loop is finished, move anchor to the next smallest number
            
    two pointers: (improvement on sorted array)
        sort the array and keep track of original indices
        start pointers at the righthand side and lefthand side 
        loop through the list
            check if the left and right pointers sum to target (if so, return True)
            if not, compare sum to target
            if sum is greater, lower the righthand (larger-value) pointer to the next lowest value
            if sum is smaller, raise the lefthand (lower-value) pointer to the next highest value
"""

# two pointers (better sorted array)
# T: O(n)
# S: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track original indices, sort as tuple, cast back to list
        length  = len(nums)
        indices = list(range(length))
        nums    = list(zip(nums, indices))
        nums.sort()
        right   = length - 1 # righthand pointer starts at the last element
        left    = 0 # lefthand pointer starts at first element
        while True: # bad form but problem description guarantees a solution
            # add left and right pointers
            res = nums[left][0] + nums[right][0]
            if res == target:
                lidx, ridx = nums[left][1], nums[right][1] # get the original indices for these numbers
                return [lidx, ridx]
            elif res < target:
                left += 1 # raise left if sum is lower than target
            else:
                right -= 1 # lower right if sum is greater than target
                    
            

# sorted array 
# T: O(n^2) at the worst, but likely much better
# S: O(n)
class __Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track original indices, sort as tuple, cast back to list
        length = len(nums)
        indices = list(range(length))
        nums = list(zip(nums, indices))
        nums.sort()
        # righthand bound is at the righthand side of the list
        larger = length - 1
        # find suitable pair
        while larger > 0:
            smaller = 0
            while smaller < larger:
                res = nums[larger][0] + nums[smaller][0]
                if res == target:
                    # translate to the original indices
                    smalleridx, largeridx = nums[smaller][1], nums[larger][1]
                    return [smalleridx, largeridx]
                smaller += 1
            larger -= 1
            

# hash map
# T: O(n) (as long as the hash lookup is O(1))
# S: O(n) (space for the hash map)
class __Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # python dict
        for i in range(len(nums)):
            current = nums[i]
            if current in hashmap:
                return [hashmap[current], i]
            complement = target - current
            hashmap[complement] = i
                    

# brute force
# T: O(n^2)
# S: O(1)
class __Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(0, i):
                r, c = nums[i], nums[j]
                # print(c, ", ", r)
                res = r + c
                if res == target:
                    return [i,j]