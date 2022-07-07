"""
thinking:

    breadth first search?
    dynamic programming?
    
    let's think about potential simplest cases
    if we have 4 houses, [1,2,3,1] gives indices 0 1 2 3
    for any index we pick, we can't pick the ones next to it
    no house has negative money so we can assume we either pick the first index or we don't (because there's no penalty to selecting as many houses as possible)
    we could treat this as continually smaller pieces
    
    say, a recursive function
        at each "chunk" of analysis, we can either pick the index i+2 (skip one house) or i+3 (skip two houses)
        these are the only two needed cases because i+2 keeps the current skipping pattern and i+3 skips an extra one so that we can shift the skipping pattern. make sense?
        

approach:
    
    recursively find max:
        function is passed nums
            base case: nums length is 1 -> return nums[0]
            check two cases: we start on nums[0] or we start on nums[1], storing these in temp vars
            in case of nums[0]: recurse on nums[2:] (because 2 means we skip nums[1], the minimum num of houses to skip)   
                                and recurse on nums[3:] (skip two houses, shift the skipping pattern)
            in case of nums[1]: recurse on nums[3:]
                                and recurse on nums[4:]
            here we want to find the larger of:
                nums[0] + max(recurse(nums[2:]), recurse[nums[3:]])
                nums[1] + max(recurse(nums[3:]), recurse(nums[4:]))
            return that max
            T: O()
            S: O()
            
            note that this will explore the same subpath multiple times
                I'm struggling to visualize how we can space-efficiently store a DP matrix
                    i.e. how do we represent a path? heh, can we represent this with binary? 1 = robbed house, 0 = did not rob
                
            

"""

# recursive
# Works, but it TLEs on larger test cases
# T: O(n^2, roughly?) it's hard to calculate exactly because we have 2 children for each "node", but one of those children was a 2-house skip, which shrinks the number of children it will have, and so on and so forth
# normally a binary tree size is 2^n
# but each level isn't n options, it's n-i options
# S: O()
class __Solution:
    def rob(self, nums: List[int]) -> int:
        count = 0
        def recurse(nums: List[int]) -> int:
            nonlocal count
            count += 1
            print(count)
            n = len(nums)
            if n == 1:
                return nums[0]
            maxMoney = 0
            for i in [0,1]:
                rest = recurse(nums[2+i:]) if n > 2+i else 0
                maxMoney = max(maxMoney, nums[0] + rest)
            return maxMoney
        # main
        print(len(nums))
        return max(recurse(nums), recurse(nums[1:])) if len(nums) > 1 else nums[0]
        
        

# exploring the official solutions

# recursion plus memoization
# T: O(N) we do at most n recursive calls, because recursive calls to indices that already have a computed value get truncated - we just return the stored value
# S: O(N) because we only create a DP list equal to the length of the nums list
class __Solution:
    def rob(self, nums: List[int]) -> int:
        # init dp map
        dp = {}
        # helper function
        def robFrom(i: int, nums: List[int]) -> int:
            if i >= len(nums): # base case
                return 0
            if i in dp: # check for precomputed result
                return dp[i]
            # check the result for robbing both current index and skipping two, vs not robbing current index and skipping one
            downstreamSum = max(robFrom(i+1, nums),
                     robFrom(i+2, nums) + nums[i])
            # store the result, i.e. the max result we can obtain at this index by starting from the end index moving inwards
            dp[i] = downstreamSum
            return downstreamSum # this will be sent back to the function that called it
        # main
        return robFrom(0, nums)
        
        

# rethinking my original solution now that I've seen the DP solution
class __Solution:
    def rob(self, nums: List[int]) -> int:
        numOfHouses = len(nums)
        dp = [-1] * numOfHouses
        def recurse(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            if dp[numOfHouses-n] > -1:
                return dp[numOfHouses-n]
            skipCurrent = recurse(nums[1:]) if n > 1 else 0
            robCurrent = recurse(nums[2:]) + nums[0] if n > 2 else nums[0]
            dp[numOfHouses-n] = max(robCurrent, skipCurrent)
            return dp[numOfHouses-n]
        # main
        return recurse(nums) if len(nums) > 1 else nums[0]
        

# tabular dp, bottom-up
# T: O(n) because we iterate over the list once
# S: O(n) for the dp list
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [None] * (n+1)
        dp[n], dp[n-1] = 0, nums[n-1]
        # populate dp 
        for i in range(n-2, -1, -1): # because we already computed the last two elements
            dp[i] = max(dp[i+1], dp[i+2] + nums[i]) # this is the "do I use the current and skip 2, or skip the current and use next?" question that we ask in the other solutions as well
        return dp[0]
    
# the third official solution shows how since we only use at most two spaces in the table, we can swap "dp[i+1]" and "dp[i+2]" for "rob_next" and "rob_current_then_skip"
