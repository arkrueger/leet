"""
approach:
    BFS: with list
        actually don't use a deque
        instead, append each level to a list within a list -> result is list of lists
            starting with root,
                for each node in the current inner list:
                    append its children (left, right) to a growing new list
                once done with the current inner list, append that new list to the end of the outer list
                then move the loop forward to the next inner list (which will be that new list)
            in this way, we layer down lists by tree level
    
    BFS: with deque
        use a deque
        init deque with the root node inside of a list
        while the deque is not empty:
            popleft -> get a list
            iterate through the list:
                append each node's val to a new growing list
                append each node's left and right children to another new growing list
            append the value list to the results list
            append the node children list to the right side of the deque
        return result

also see https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS with deque (is it possible?)
# T: O(n)
# S: O(w) where w is the level width (number of nodes at each level)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q = deque([root])
        res = []
        while q:
            level       = q.popleft() # list of current level nodes
            nextNodes   = [] # list of next level nodes (current level's child nodes)
            levelVals   = [] # list of current level vals
            for node in level:
                if node:
                    levelVals.append(node.val)
                    nextNodes.append(node.left) if node.left else None
                    nextNodes.append(node.right) if node.right else None
            res.append(levelVals) if levelVals else None
            q.append(nextNodes) if nextNodes else None
        return res


# BFS with list of lists
# T: O(n) 
# S: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root]]
        i = 0 # outer loop index
        while i < len(res): # length of res will grow until we have filled all levels
            nextLevel = []
            for node in res[i]:
                if node is not None:
                    nextLevel.append(node.left) if node.left else None
                    nextLevel.append(node.right) if node.right else None
            if nextLevel: # don't append an empty level
                res.append(nextLevel)
            i += 1
        return [[e.val for e in x] for x in res]
    
    
    
    
    
    