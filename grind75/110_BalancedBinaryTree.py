### GRIND 75 SECOND PASS ###
"""
approach:
    recursive:
        ask left and right child nodes about their height
        compare heights: good to go if their heights differ by < 2
        ask left and right if their children *also* were balanced (this will avoid hidden imbalances)
        return True if these three cases are true
        base case: return True if root is None
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# T: O(n)
# S: O(n) for recursive space
class Solution:   
    class Height:
        def __init__(self):
            self.height = 0
    def isBalanced(self, root: Optional[TreeNode], height: Height=None) -> bool:
        if root is None:
            return True
        # heights
        leftHeight = self.Height()
        rightHeight = self.Height()
        
        # recurse on left and right children (aka ask if they are balanced) -> bool
        leftBalanced = self.isBalanced(root.left, leftHeight)
        rightBalanced = self.isBalanced(root.right, rightHeight)
        
        # compute the height of the current node from the children
        if height: # height was passed in by reference on recursion (=None on first function call)
            height.height = 1 + max(leftHeight.height, rightHeight.height)
        
        # we want to check two things here:
        # 1) are the heights of my left and right child's subtrees within 1 of each other?
        # 2) was the same true for their children? (i.e. avoid hidden imbalances)
        if abs(leftHeight.height - rightHeight.height) < 2:
            return (leftBalanced and rightBalanced) # will be True if left and right are balanced + their children are balanced
        
        # if we haven't returned by now, the tree is not balanced
        return False

    
# post-order traversal (found this one in the forum)
# T: O(n) number of nodes in the tree
# S: O(?) I'm inclined to say O(n) space complexity because of the depths dict
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else: # if the node we examined on the last iteration was a leaf, then its children are None
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True