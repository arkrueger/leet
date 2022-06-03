# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
approach:
    recursive:
        check if child left < node < child right
        ask each child if the same is true
        base case - node is null
        
        
    DFS:
        hmm, how do we establish the min/max as we traverse the tree?
            -> do this by making the DFS stack hold a tuple as (node, lower bound, upper bound)
                recall that right child has root as lower bound, and inherits its upper bound from root
                            left child inherits its lower bound from root, and has root as upper bound
                            
    BFS:
        same deal as DFS, but use a deque instead of a stack and popleft to get current node
    
"""

# BFS
# T: O(n) n is number of nodes
# S: O(n) node deque space
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        q = deque([(root, -math.inf, math.inf)])
        while q:
            node, lower, upper = q.popleft()
            if node:
                # check if the constraints are violated -> return False
                if node.val <= lower or node.val >= upper:
                    return False
                # pattern (node, lower bound, upper bound)
                left = (node.left, lower, node.val) 
                right = (node.right, node.val, upper)
                q.append(left); q.append(right)
        return True

# DFS
# T: O(n) n is number of nodes
# S: O(n) node stack space
class __Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, lower, upper = stack.pop() # lower/upper are the bounds (parent node & inherited)
            if node:
                # check if the constraints are violated -> return False
                if node.val <= lower or node.val >= upper:
                    return False
                # pattern (node, lower bound, upper bound)
                left = (node.left, lower, node.val) 
                right = (node.right, node.val, upper)
                stack.extend([left, right])
        return True


# recursive
# T: O(n) where n is number of nodes
# S: O(n) recursive space
class __Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root: Optional[TreeNode], lower, upper) -> bool:
        # base case
        if root is None:
            return True
        # note on lower and upper bounds (narrows as we go deeper in the tree)
        # for left child, upper bound is root and lower bound is inherited
        # for right child, lower bound is root and upper bound is inherited        
        if root.left:
            left = root.left.val 
            if left >= root.val or left < lower:
                return False   
        if root.right:
            right = root.right.val
            if right <= root.val or right > upper:
                return False
        rightValid = self.helper(root.right, root.val+1, upper)
        leftValid = self.helper(root.left, lower, root.val-1)
        return leftValid and rightValid    

# recursive - rewritten more concisely
# T: O(n) where n is number of nodes
# S: O(n) recursive space
class __Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)
    
    def helper(self, root: Optional[TreeNode], lower=-math.inf, upper=math.inf) -> bool:
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        rightValid = self.helper(root.right, root.val, upper)
        leftValid = self.helper(root.left, lower, root.val)
        return leftValid and rightValid
