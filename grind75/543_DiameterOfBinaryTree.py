# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
approach:
    the longest path will be from one leaf to another
    we can look at this as the path from one leaf to another, through an intermediate root node
        this root node does not have to be the overall root node, but it will be the highest node level in the path
    for this solution we can modify the "height of tree" method
        the height of tree method finds the maximum height from root to leaf by recursion (return 0 if null, return 1+max(rightHeight,leftHeight) if node is not null)
    
    we want to recurse down the tree,  
        getting the length from the furtherst lefthand leaf to the furthest righthand leaf
            ^ let's call that distance the diameter for a given node
        -> recursion should return the maximum of: the current node's "diameter",  its lefthand child's diameter, and righthand child's diameter
        
    
"""
class Solution:
    # Correcting my original solution after peeking at the forum
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dp = self.DP(-1) # for accessing max height across function calls for DP
        self.findMaxPath(root, dp)
        return dp.maxPath - 1 # why - 1?
    
    def findMaxPath(self, root: Optional[TreeNode], dp) -> int:
        if root is None:
            return 0
        # recurse to get the heights
        lHeight = self.findMaxPath(root.left, dp) 
        rHeight = self.findMaxPath(root.right, dp)
        
        currentHeight = max(lHeight, rHeight) + 1 # the height of the current node
        leftRightPath = lHeight + rHeight + 1 # the max path between furthest leaf nodes on left and right
        currentMaxPath = max(currentHeight, leftRightPath) # ?
        dp.maxPath = max(currentMaxPath, dp.maxPath) # the overall max length path
        
        return currentHeight # why height? because we recurse to get the height (we dp-ref to store the overall max)
        
    class DP:
        def __init__(self, x: int):
            self.maxPath = x
            
    
    
    # My original solution below, fails the second to last test case
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get the max possible leaf-leaf path of the current node
        # get the max possible leaf-leaf path of the left and right children
        maxHere     = self.helper(root)
        maxLeft     = self.helper(root.left)
        maxRight    = self.helper(root.right)
        # return the max of the three
        maxOfChildren = max(maxLeft, maxRight)
        return max(maxOfChildren, maxHere)
    
    # gives us the max path from leaf to leaf considering current node as root
    def helper(self, root: Optional[TreeNode], firstCall: Optional[bool]=True) -> int:
        # return 0 if root is null
        if root is None:
            return 0
        # otherwise, recurse to get child node heights
        lHeight = self.helper(root.left, False)
        rHeight = self.helper(root.right, False)
        
        # if this was the first call in the recursive chain
        if firstCall:
            return lHeight + rHeight
        
        # return height at this node
        return 1 + max(lHeight, rHeight)
    """
