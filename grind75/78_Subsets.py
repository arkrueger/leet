"""
approach:
    
    brute force:
        try all combinations, using a set of frozensets
        
    dynamic programming bottom up:
        T: O(n!)
        S: no additional structures created but output list occupies n! space
        start with the zero-combination (trivial)
        then build the 1-combinations
        then build the 2-combinations using the 1-combinations
        then build the 3-combinations using the 2-combinations
        
        mapping it out:
            nums = [1,2,3,4]
            0: []
            1: [1],[2],[3],[4]
            2: [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
            3: [1,2,3],[1,3,4],[1,2,4],[2,3,4]
            4: [1,2,3,4]
        in steps, this is:
            0: []
            1+: for each c in prev step, build combos that extend with each nums[i] greater than c[-1]
        stop when len(combo) == len(nums)
        
    breadth first search:
        sort nums ascending
        treat nums as an n-ary tree where for each node, n is len(n)-index(n)
        in other words, each node's children must be greater in value than that node
            (this will prevent duplicates)
        use a queue initialized with [] empty list
        while the queue is not empty:
            pop left into current
            build all valid combinations, extending current with all values of num greater than current[-1] (the last value in the current combo, which is guaranteed to be largest in the combo)
            append all combinations (or their indices in the output array) onto the queue
            the queue runs empty when there are no elements in nums greater than current[-1]
        
"""

# dynamic programming bottom up
# it could also be thought of as BFS in the sense that instead of popping left and appending to queue, we simply view left (using tail) and append to queue
# T: O(n!) ? maybe, could also be O(n*2^n)
# S: O(1) not including output array
class __Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        combos = [[]]
        tail = 0 # this will point to our spot in the previous step (see pseudocode for expl.)
        while tail < len(combos):
            for v in nums:
                if combos[tail] == [] or v > combos[tail][-1]: # on first iteration, combos[0][end] is None, after the first iter we want to add only v-values greater than the current end value
                    combos.append(combos[tail]+[v])
            tail += 1
        return combos
                    
    
# BFS
# essentially the same thing as the DP example above (if it's even DP) but instead of preserving the queue as the output, we store it separately
# this is the less efficient and less readable
# T: O(n!)
# S: O(n!) for the queue
class __Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        q = deque([])
        combos = [[]]
        while True:
            if not q: pass
            else: combos.append(q.popleft())
            for v in nums:
                if combos == [[]] or v > combos[-1][-1]:
                    q.append(combos[-1]+[v])
            # still salty that python doesn't have a do-while loop
            if not q:
                break
        return combos

            

# another one I saw on the forum
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        combos = [[]]
        # build the list
        for n in nums:
            combos += [c + [n] for c in combos]
            # above builds [1],[2],[3], then [1,2],[1,3],[2,3] then [1,2,3]
        return combos
