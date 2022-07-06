"""
approach:
    naive/brute force:
        iterate through the array, store element frequencies in a dict
            check if frequency > floor(n/2) -> return that element
    
    Moore's voting algorithm:
        we have our array of values
        also create the variables val and count
            val will hold the value of the candidate element (the one that might be the majority)
            count will hold the current tally of number of times we have encountered val
                (see next for clarity / how it works)
        background concept:
            if a value is in the majority, its count is greater than all other counts combined
            -> if we iterate over the array, we can count (heh) on seeing majority more times
            we can exploit this property as a "weight" for the majority element
        store the first element in val, set count to 1
        iterate over the array
            on each iteration, increment count if elem = val (this "weights" val)
            decrement count if elem != val (again, "weights" val)
            if count == 0, then (at least for now) we have no reason to assume val is the majority
                -> set val to the current element and count to 1, continue iterating
            in this way, because the majority will accumulate more increments than decrements,
                (because count(maj) > count(all others combined) ) we ensure that val will be set to 
                the majority element when we finish the loop
        iterate over the array to count the instances of majority val to confirm that it was maj
            (if there was no majority, the algo would still give a value, so we need to confirm)
        
            
"""

# Moore's algorithm approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # holder vars
        count = 1
        val = nums[0]
        # iterate to identify majority candidate
        for x in nums:
            # accumulate or ... decumulate? deaccumulate? 
            if x == val:
                count += 1
            else:
                count -= 1
            
            # reset if current val's gains are wiped out
            if count == 0:
                val = x
                count = 1
        # assuming majority exists in the array, so returning the candidate
        return val
        
        ### OPTIONAL ###
        # for this problem, we could assume that the majority element exists in the array
        # but outside this question, we would want to verify that the candidate is actually majority
        count = 0 # reuse the count variable
        for x in nums:
            if x == val:
                count += 1
        if count > (len(nums) / 2):
            return val
        return -999 # example flag we might use if there was no majority
        
        
        
        

# Map-based approach
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         d = {}
#         half = len(nums) / 2 # floor div
#         for i in nums:
#             # increment frequency
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#             # check if majority
#             if d[i] > half:
#                 return i
