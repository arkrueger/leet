"""
thinking:

    opportunities:
        two pointers?
        dp ?
        
    extra space but more efficient compute: # nope, this doesn't work because smaller but further but still warmer temps can hide closer even warmer temps
        iterate over the array once
        store temps as keys, values are arrays of indices where the temps occur
        might need to store a sorted array of keys so we know what the next warmest key value is
        iterate over the temperatures array again
            find the next warmest temp (if none, set ans[i] to 0)
            use that as a key to get its index array, bisect_right to find the earliest index of that temp after the temperatures[i] temp
            if none exists, search for the next warmest until there are no keys left
        
    
    mapping out:
        
        [73,74,75,71,69,72,76,73]
        [73,74,75,71,69, 1, 0, 0]
        [1, 1, 4, 2, 1, 1, 0, 0 ] filling in order
        
        [73,74,75,71,69,72,76,73] temps         then sort to get [69, 
        [0, 1, 2, 3, 4, 5, 6, 7 ] indices                           
        
        

approach:

    brute force:
        T: O(n^2)
        S: O(1)
        iterate over the array with pointer i
            iterate over the array (nested) with pointer j
                if temps[j] > temps[i], set ans[i] = j - i
                    foundWarmer = true
                    break
            if not foundWarmer, set ans[i] = 0
        return ans

    monotonic stack:
        mapping it out
            [73,74,75,71,69,72,76,73]
            stack                   prev (day, temp)     curr (day, temp)       curr > prev     ans[i]
            0                       0, 73                   1, 74               y               1
            1                       1, 74                   2, 75               y               1
            2                       2, 75                   3, 71               n               -
            2, 3                    3, 71                   4, 69               n               -
            2, 3, 4                 4, 69                   5, 72               y               1
            2, 3                    3, 71                   5, 72               y               2
            2, 5                    5, 72                   6, 76               y               1
            2                       2, 75                   6, 76               y               4
            6                       6, 76                   7, 73               n               -
            we never check the last index because it's appended to the stack at the end of its iteration, then the for loop exits
            

    reverse iterative:
        # our process is like this: 
        #   keep track of our offset from the current index, i
        #   increment offset and check temps[i+offset] -> is it warmer? if so, return offset - i
        #   if not warmer, set offset += ans[i+offset] so that temps[i+offset] now yields the next temp warmer than the previous checked temp
        #   repeat the process
"""

# reverse monotonic stack with less space, official solution
# T: O(n) 
# S: O(1) because the output array doubles as a processing data structure
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init our answer array
        n = len(temperatures)
        ans = [0] * n
        # iterate in reverse
        for i in reversed(range(n-1)): # -1 b/c we know ans[-1] = 0, b/c there are no days after the last day
            offset = 1
            while i+offset < n:
                if temperatures[i+offset] > temperatures[i]: # we found a warmer day
                    ans[i] = offset
                    break # to avoid overwriting and save compute
                elif ans[i+offset] == 0:
                    break # if we reach here, then temps[i+offset] is lower than current temp; if temps[i+offset]==0 then there is no warmer temp than that temp, which is lower than the temp we're trying to find an answer for, so there can't be a warmer temperature, so break and leave as zero
                offset += ans[i+offset] # skip over (nonmonotonic-agnostic) decreasing regions to the next potential answer
        
        return ans      
            


# monotonic stack, official solution
# T: O(n)
# S: O(m) where m is the longest monotonically decreasing region, this could be simply "n" if the entire list is monotonically decreasing
class __Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        # stack time
        for currDay, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp: # this does not run on the first iteration
                prevDay = stack.pop()
                ans[prevDay] = currDay - prevDay
            stack.append(currDay) # this runs on the first iteration, which starts the stack traversal off with the first element
        # outdent
        return ans


# brute force
# works, but TLEs on the larger test cases
class __Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        foundWarmer = False
        for i in range(len(temperatures)):
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    foundWarmer = True
                    ans[i] = j-i
                    break
            ans[i] = ans[i] if foundWarmer else 0
            foundWarmer = False
        # end nested
        return ans
