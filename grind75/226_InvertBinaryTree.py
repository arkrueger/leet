### GRIND 75 SECOND PASS ###
"""
inverting a binary tree means swap the left and right child nodes

approach:
    recursive:
        base case, return if node is null
        if node is not null
            swap left and right children
            recurse both children
    
    stack: 
        https://leetcode.com/problems/invert-binary-tree/discuss/62707/Straightforward-DFS-recursive-iterative-BFS-solutions
    
    BFS:
        use a deque
        put the root node in the deque
        while the deque is not empty:
            popleft on deque
                swap its child nodes
                append the child nodes to the right of the deque
                continue
                -> because we pop the left and append to the right, we will traverse each level before we start on the next level
    
    DFS:
        use a stack this time
        it's a similar idea to the bfs
        but unlike BFS, don't append to the right, append to the left
            wait, but won't we end up double dipping? Nope! because we aren't adding any node twice, we aren't swapping twice
                -> we swap, then we add to the list to grab the children
                the main mechanism that drives the difference here is the appending&popping on the same side rather than FIFO
        
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# T: O(n)
# S: O(d) where d is the depth of the tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root


# BFS
# T: O(n) 
# S: O(k) where k is the number of leaf nodes, or 2^(number of levels-1)
class __Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        q = deque([root])
        while q:
            node = q.popleft()
            if node: # sometimes this will be null if we added a leaf node's "children" to the deque
                node.left, node.right = node.right, node.left
                # append the child nodes so that we pop them on a later iteration
                q.append(node.left)
                q.append(node.right)
        return root


# recursive
# T: O(n?) where n is the number of nodes in the tree
# S: O(n?) where n is the number of nodes in the tree
class __Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root
    
    def helper(self, node: Optional[TreeNode]) -> None:
        # base case
        if node is None:
            return
        swap = node.right
        node.right = node.left
        node.left = swap
        self.helper(node.left)
        self.helper(node.right)