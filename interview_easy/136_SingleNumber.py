"""
note: the problem asks for constant space, but seeing as integers appear at most twice, any hash table or set (even if it's in a one-liner) that we create will be O(n/2) space. I disagree that the official solutions provided obey the O(1) constraint (or that it's even possible to do in O(1) space)

approach:
    frequency dict: (linear complexity but O(n) in space, which the problem bars)
        init a dict to store integer frequencies
        loop over the array and store these frequencies
        loop over the dict and return whichever integer key indicates a freq of 1        
    
    math:
        from the official solution
        a bit on the "how would I know that proof/algorithm" side for interviews
            but it's very logical and obvious once you see it
        imagine we can know what the missing number is and place it in the array
        then we sum the array - call this "complete sum"
        we also of course have our actual array, the one with the missing number
        sum this to get the "incomplete sum" 
        it's straightforward to say at this point that the missing number is:
            complete sum - incomplete sum
        it's a simple calculation, we just need to get "complete sum" and "incomplete sum"
        complete sum: cast the list to a set, sum the set, and multiply by 2 (set removes duplicates, but since our missing number appears once it will still be in the set)
        incomplete sum: sum the original list
"""

# set math - from leetcode's official solution
# T: O(2n) -> O(n)
# S: O(n/2)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)


# frequency dict
# T: O(n)
# S: O(n/2) because each integer appears twice except for one, which appears once
class __Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for f in freq:
            if freq[f] == 1:
                return f
