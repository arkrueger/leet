"""
thinking:
    
    I think I've seen and solved this problem before
        let's see if I can do it more quickly this time
    
    at a glance, we can see some similarities to the "Valid Parentheses" problem
        kinda surprised to see that it's not in the similar questions list
        if we give all of the numbers in the intervals labels as "opening" and "closing"
            then deconstruct the intervals and sort the numbers
            then push all of these onto a stack (or deque, just changes which direction we sort)
        then, if we see two openers in a row, then we know we're about to see an overlap
    
    we can probably also sort the intervals list based on the openers
        at each interval, check if the next opener < current closer -> that's an overlap
    
approach:
    
    stack:
        see inline comments
    
    traversal with indexing:
        sort the intervals list based on the 0th element in the inner lists
            in python this is a simple intervals.sort() (no fancy lambdas needed)
        traverse the list
            for each inner list intervals[i], check if intervals[i+1][0] < intervals[i][1]
                (i.e. if next opener is less than current closer)
            merge the intervals
        two choices here for output:
            1) could edit the intervals list directly (but that could introduce additional time complexity when elements need to be deleted to merge intervals)
            2) could create a new intervals list (more space, but better runtime if the input has a lot of overlaps)


"""

# from the solution
# T: O(n*logn)
# S: O(n or logn) depends on how python does sorting built in
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # since intervals is sorted and we can edit merged in place, init to first interval
        merged = [intervals[0]] 
        for r in intervals: # no need to skip the first interval b/c it will overwrite its closer
            if merged[-1][1] < r[0]:
                merged.append(r)
            else:
                # this takes care of fully contained intervals, too 
                merged[-1][1] = max(merged[-1][1], r[1])
        return merged


# stack
# T: O(n*logn) where n is intervals list length (why n*logn? because of the sorting step)
#       the merging portion is just T: O(n)
# O: O(n) for the tagged list
class __Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tags = [i%2 for i in range(2*len(intervals))] # 0 : opener, 1: closer
        intervals = [x for i in intervals for x in i] # flatten the intervals list
        stack = list(zip(intervals, tags)) # pair open/close tags with interval numbers
        stack.sort(reverse=True) # sort the interval nums
        
        merged = []
        count = 0
        opener = None
        while stack:
            opener = stack.pop() if opener == None else opener
            nxt = stack.pop()
            if nxt[1] == 0:
                count += 1
            else:
                if count == 0:
                    merged.append([opener[0], nxt[0]])
                    opener = None
                    continue
                count -= 1
        return merged
                
    
# traversal with indexing
# T: O(n*logn) where n is intervals list length (why n*logn? because of the sorting step)
#       the merging portion is just T: O(n)
# O: O(o) where o is the size of the output array (will be smaller than n)
class __Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        merged = []
        intervals.sort()
        print(intervals)
        while i < n:
            opener, closer = intervals[i]
            # build the interval
            while i < n-1 and intervals[i+1][0] <= closer:
                closer = max(closer, intervals[i+1][1]) # keep the largest closer in this merge
                i += 1
            # keeps current closer if the i+1 etc interval(s) wholly contained in the first interval
            closer = max(closer, intervals[i][1]) 
            merged.append([opener, closer]) 
            i += 1
        
        return merged
