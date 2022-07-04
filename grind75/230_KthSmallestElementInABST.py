"""
thinking:
    
    problem mentions 1-indexed, so the kth smallest is actually the kth smallest
    properties of BST:
        left child (and all descendants) are lower, right etc are higher
        
approach:
    
    brute force:
        could follow the left children all the way down and find the smallest
        then traverse in order until we find the kth largest
    
    slightly smarter:
        recursively search using in order traversal
            on base case (no child nodes) return 1
        return the node where the recursive return value is k-1
        even better than a recursive return would be an external variable 
            doesn't begin incrementing until the smallest value is reached
        T: O(n) where n is the number of nodes
        S: O(h) where h is the height of the tree for the recursive call stack
        



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# depth first search
# T: O(n)
# S: O(h)
class __Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(root: Optional[TreeNode]):
            nonlocal k; nonlocal kthSmallest
            if root is None:
                return False
            # search the lefthand side first
            if search(root.left) :
                return True
            # the k decrement step will only be run once we hit the leftmost descendant 
            # because we recurse left before decrementing
            # this allows us to decrement k as we traverse in order, i.e. k hits 0 when we reach the kth smallest node
            k -= 1
            # check for exit case
            if k == 0: 
                print("i ran hello")
                kthSmallest = root.val
                return True
            # since we didn't find it in the left, search the righthand side
            search(root.right)
        
        # main
        kthSmallest = -1
        search(root)
        return kthSmallest
        
        
# for comparison, the official solution is even more compact but requires extra space
# depth first search
# T: O(n) as expected for DFS, though note that they visit all nodes even if they find the solution early
# S: O(n) because they're storing the traversal and visiting all nodes
class __Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: Optional[TreeNode]):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        # main
        return inorder(root)[k-1]
        
# also for comparison, the official solution's iterative (stack) implementation
# provides a great example of how to prep a stack for each branch of inorder search
# T: O(h + k)
# S: O(h)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        # traversal
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
