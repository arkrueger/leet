# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
approach:
    
    recursive DFS:
        perform recursive DFS
        create an external variable passed to each function call so that the recursive return value can be decoupled from generating the solution
        
    iterative with parent pointer dict: 
        (similar to adjacency list)
        use a stack to DFS the tree, for each node do:
            dict[node.leftChild] = node
            dict[node.rightChild] = node
        to generate a map that will allow us to traverse the tree from leaf to root
        now traverse root-ward from p and q, storing their ancestors in a set
            at each traversal tick, check if p and q have any common ancestors
            as soon as they do, that common ancestor is the LCA
            return it

    solution recursive DFS:
        perform dfs, return true if p or q was found in any ancestor
        we can ascertain the quality of the current node by checking:
            is the current node p or q?
            are the children (left, right) parents of (or are) p or q?
            we call these booleans mid, left, and right
                if at least two of these are true, then the current node is the LCA
                so we check if 
            the DFS will continue to unwind
                explanation of how self.ans doesn't get overwritten:
                    since the current node is (or is parent of) both p and q, the other child must return false to its parent
                    so even though we still return True after setting self.ans, the parent will not overwrite it (because mid is False and the other child's bool is False)
        

"""

# recursive approach from the solution (different from mine)
# T: O(n)
# S: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node: 'TreeNode') -> bool:
            # base case
            if not node:
                return False
            # recursion
            left = traverse(node.left)
            right = traverse(node.right)
            # check for LCA
            mid = (node == p) or (node == q)
            if mid + left + right >= 2:
                self.ans = node
            # return True if any of (mid, left, right) are true
            return mid or left or right
        
        self.ans = None
        traverse(root)
        return self.ans
            


# iterative rootward traversal
# T: O(n) n is number of nodes in the tree (parent dict precompute: n, LCA search: depth of p or q, whichever is greater)
# S: O(n) number of nodes, worst case if p and q are both on the far righthand side of the tree
class __Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        # generate parent dict
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # find lowest common ancestor
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p] # reassign p to its parent so that we traverse root-wards
        while q not in ancestors: # as soon as q is in p's ancestors, it is the LCA
            q = parent[q] # traverse root-wards
        return q
        
        





# recursive DFS - a bit unorthodox, but will work on a non-binary tree as well 
# T: O(n) n is number of nodes in the tree
# S: O(d) d is the depth of the tree, this is space for the recursive calls
class __Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # returns "p" or "q" if it found only one of them, or "" if it did not find them
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', ans: 'TreeNode') -> 'TreeNode':
            if not root:
                return None
            
            left    = dfs(root.left, p, q, ans)
            right   = dfs(root.right, p, q, ans)
            
            # all possible combinations that indicate root is an LCA
            foundLCA = (left == q and right == p) or (left == p and right == q) or (left == p and root == q) or (left == q and root == p) or (right == p and root == q) or (right == q and root == p)
            
            if foundLCA:
                self.ans = root
                return None
            elif root == p or root == q:
                return root
            if left == q or left == p:
                return left
            if right == q or right == p:
                return right
            else:
                return None
        
        foundP = foundQ = False
        self.ans = None
        dfs(root, p, q, self.ans)
        return self.ans
