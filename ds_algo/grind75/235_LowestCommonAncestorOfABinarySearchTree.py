### GRIND 75 SECOND PASS ###

"""
Just riffing:  
    DFS and creating singly linked lists: (terrible idea)
        use DFS to find each node (p and q)
            treat the paths from root to p and root to q as singly linked lists
        loop: starting from root on both lists moving towards p and q
            check if current_node_q == current_node_p
            return, of the following, whichever is encountered first:
                current node when it is == p or == q
                previous node when current nodes are not the same
                ^ this is just semantics, but current node could be node.next and previous node could be node
        to guide the SLL from root to p / q, we'll use stacks of 0/1 to denote left/right children

approach:
    canonical solution - use BST properties:
        BST means for each node:
            left child val < node val
            right child val > node val
        we can use this to guide our path towards nodes p and q without needing to do a blind BFS/DFS
        recursively,
            if both p and q are less than current node -> recurse on left child
            if both p and q are greater than current node -> recurse on right child
            they are not both on one side (i.e. one is above, one below, or one is equal to current) -> return current
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative (boils down to the same as the recursive)
# T: O(k) k is tree depth of LCA
# S: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
# I have also seen this iterative version written as:
    def __lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root


# recursive
# T: O(k) where k is the tree depth of the lowest common ancester
# S: O(k) for the recursive space
class __Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        
        
        
        