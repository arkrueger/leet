# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

"""
approach:
    binary search:
        check mid, if bad then move area of interest to first half, otherwise second half
        confirmed that calling isBadVersion(0) returns False which means we don't need explicit edge case
        
        map out a test case
        n = 5, firstbad = 4
        1 2 3 4 5 -> high 5, low 1 mid 3
        3 4 5 -> high 5, low 3, mid 4 -> found it
        n = 6, firstbad = 4
        1 2 3 4 5 6 -> high 6, low 1, mid 3
        3 4 5 6 -> high 6, low 3, mid 4 -> found it
        fails on n = 1, firstbad = 1 because mid is always 1 so we never meet the exit case
        better to have low initialized to 0 because it hedges against this issue
        
"""
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n+1
        while True:
            mid = (low + high) // 2
            if not isBadVersion(mid):
                if isBadVersion(mid+1):
                    return mid+1    
                low = mid
            else:
                high = mid
        
        
