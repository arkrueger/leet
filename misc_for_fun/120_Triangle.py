"""
approach:
    
    brute force:
        try out all paths and keep only the minimum
    
    DFS:
        treat the triangle as a tree
        perform depth first search, record the value reached at the leaf nodes
    
    DP leaf->root traversal:
        start from the leaves and work towards the roots
        once paths merge, abandon the higher sum path in favor of the min sum path
        return the min sum path that remains at the end
        
"""

# DP leaf->root traversal
# T: O(h*b/2) where h is triangle height, b is base length (last row length)
# S: O(1) because we destroy the input instead of using a temp array
class __Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # edge case where we don't have a triangle
        if len(triangle) < 2:
            return 0 if len(triangle) < 1 else triangle[0][0]
        # we're going to modify the input in place
        for r in range(len(triangle)-2,-1,-1): # start at second to lowest row 
            for c, v in enumerate(triangle[r]):
                triangle[r][c] = v + min(triangle[r+1][c], triangle[r+1][c+1])
        return triangle[0][0]
    

# ALTERNATIVE: if we are not allowed to destroy the input
# DP leaf->root traversal
# T: O(h*b/2) where h is triangle height, b is base length (last row length)
# S: O(b) where b is triangle base (last row length) for the temp array
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # edge case where we don't have a triangle
        if len(triangle) < 2:
            return 0 if len(triangle) < 1 else triangle[0][0]
        # temp storage for the minimum sums, will be updated row-by-row
        temp = [i for i in triangle[-1]] # same length as the base
        for r in range(len(triangle)-2,-1,-1): # start at second to lowest row 
            for c, v in enumerate(triangle[r]):
                temp[c] = v + min(temp[c], temp[c+1])
        return temp[0]
