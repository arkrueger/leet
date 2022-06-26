"""
thinking:
    
    the amount of water a container can store can be thought of as
        the distance from one container edge to the nearest equal or taller other edge on either side
        times the height of the starting container edge
    
    From this perspective, having the heights sorted would be useful
    -> hash map of key:value as height:index
    from this we can traverse forward in the array until we find two key value pairs that satisfy
        key < current, index > current -> one index past the potential container edge on the right
        key < current, index < current -> same idea, but on the left
        decrement to the previous item to get left and right container walls
        the water amount is current_height*(current_index-left_index) and current*height(right_index-current_index)
        if greater than max, store in max
        
    another thought is that we could use two pointers starting from the outer edges
    the idea being that if we encounter any shorter walls inside of larger walls, their water amounts can't possibly exceed the taller walls that are farther apart
    so loop and walk the two pointers inwards calculating water volume, abandoning current walls for bigger walls wherever encountered
    water volume is min(left_edge, right_edge)*(right_index - left_index)
    in addition to the pointers to the preserved container edges, we will want "scouts" moving ahead to compare new edges to the current edges
    
    let's map out this idea with example 1 input:
        left        right   volume
        1           7       8
        8           7       49
        8           8       40
        
        49 is our max
        

approach:
    
    two pointers:
        i, j = 0, n-1
        left_edge, right_edge = 0, 0
        left_index, right_index = 0, n-1
        while l < r:
            if height[i] > left_edge:
                left_edge, left_index = height[i], i
            if height[j] > right_edge:
                right_edge, right_index = height[j], i
            compute water volume
            store in max if it's a new max
        return max water volume seen
        T: O(n)
        S: O(1)


"""

# two pointers
# T: O(n) 
# S: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        left_edge, right_edge = 0, 0
        left_index, right_index = 0, n-1
        mostWater = 0
        # calculate the max
        while i <= j: # i is on the left, j on the right
            if height[i] > left_edge:
                left_edge, left_index = height[i], i
            if height[j] > right_edge:
                right_edge, right_index = height[j], j
            mostWater = max(mostWater, min(left_edge, right_edge)*(right_index - left_index))
            # choose which pointer to move forwards
            if left_edge < right_edge:
                i += 1
            else:
                j -= 1
        return mostWater
