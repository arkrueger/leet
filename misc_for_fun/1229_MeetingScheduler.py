# doing this after solving in pramp practice interview
# solution will probably be slightly different because leetcode has more edge cases
"""
thinking:
    
    what quality defines a compatible set of availabilities?
    laterStart = max(1start, 2start)
    earlierEnd = min(1end, 2end)
    compatible = laterStart <= laterStart + duration <= earlierEnd
    
approach:
    
    brute force:
        try all combinations with nested for loops
        return the first seen compatible overlap
    
    intelligent indexing:
        create two indexes, i for slots1 and k for slots2
        loop while i and k are both in bounds for their lists
            check if there is an overlap in slots1[i] and slots2[k]
                (i.e. if both interval ends are later than the other interval's start)
                if not, then increment the index of the one that is further behind by 1 and continue
            if there is an overlap,
                check the conditional described at the end of the "thinking" section above
                if the conditional is true, return the interval [laterStart, laterStart + duration]
        return [] if we traversed both lists without finding a compatible interval
"""

# smart indexing
# T: O(n) where n is the longer list
# S: O(1)
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # why wouldn't we get sorted lists?
        # popular opinion:
        # when the input is in a non-ideal order, and putting it in ideal order is a trivial 2-liner, it didn't add any value to the problem by having the input in a non-ideal order
        slots1.sort()
        slots2.sort()
        # indices
        i = k = 0
        # loop
        while i < len(slots1) and k < len(slots2):
            start1, start2  = slots1[i][0], slots2[k][0]
            end1, end2      = slots1[i][1], slots2[k][1]
            # make the intervals level with each other if one is ahead of the other
            if end1 < start2: # move 1 forward
                i += 1
                continue
            if end2 < start1: # move 2 forward
                k += 1
                continue
            # check if they are compatible (return if so)
            laterStart = max(start1, start2)
            earlierEnd = min(end1, end2)
            compatible = laterStart <= laterStart + duration <= earlierEnd
            if compatible:
                return [laterStart, laterStart + duration]
            # increment the index of the earlier-ended interval
            if end1 < end2:
                i += 1
            else:
                k += 1
        # return empty array if no compatible meeting time was found
        return []

    
# brute force, gets TLE
# T: O(n^2)
# S: O(1)
class __Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        ans = []
        for one in slots1:
            for two in slots2:
                start1, start2  = one[0], two[0]
                end1, end2      = one[1], two[1]
                laterStart = max(start1, start2)
                earlierEnd = min(end1, end2)
                compatible = laterStart <= laterStart + duration <= earlierEnd
                if compatible:
                    ans.append([laterStart, laterStart + duration])
        ans.sort() # so that the earliest goes to the start
        # return empty list if we didn't find a match
        return ans[0] if ans else []
