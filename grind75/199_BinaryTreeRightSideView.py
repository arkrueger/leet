"""
thinking:
    
    
    seems simple from the illustration
    but what if the right-most chain is short? then we would see things that come from the left
    I see it like this:
        we want to return something from every level (depth) of the tree
        for each level, we want to return the rightmost node
    
    we could use breadth first search for this 
        or depth first search 
        I think they will be equally efficient because we need to visit the entire tree regardless
            in order to find any potential degenerate tree hangnails that increase the depth
            though if we were given tree depth, BFS would be more efficient for a left skewed tree, whereas DFS would be more efficient for a right skewed tree
    what truths can we use to our advantage here?
        we will only return one node for each level
            -> once we find the rightmost node for a level, we can disregard the other nodes at that level (to be clear though, we still must visit their children)
    if we design our search pattern to always find the rightmost nodes first
        then we can iteratively search for nodes in level x, then increment x once a righthand-visible node is found
    
    approach:
        
        depth first search:
            using a stack or recursion, search the tree using reverse preorder traversal
                (reverse preorder is root, right, left, repeat)
                current_level - level we are currently visiting
                seek_level - level we need a visible node for
                build the stack as a pair (node, current_level) so we can track the node's level
                as soon as we find a node
                    append the node's value to the result list
                    increment seek_level
            exit loop when stack is empty
            return result list
        
        breadth first search:
            pretty much the same as DFS but will take
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# depth first search - iterative
# T: O(2^h) h = tree height, because we traverse the entire tree
# S: O(h) for the stack
class __Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return [] 
        stack = [(root,0)]
        res = []
        seek = 0 # level we need to find a visible node for
        while stack:
            node, level = stack.pop()
            if level == seek:        # we found the rightmost node at this level
                res += [node.val]   # throw it on the result list
                seek += 1           # seek the next level down
            # visit children - because stack pops in reverse order, we want to append the left child, then the right (so that we pop the right first on the next iteration)
            if node.left:
                stack += [(node.left,level+1)]
            if node.right:
                stack += [(node.right, level+1)]
        return res
    

        
# depth first search - recursive
# T: O(2^h) h = tree depth, because we traverse the entire tree
# S: O(h) recursive stack
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return None
            if level == self.seek:
                self.res += [root.val]
                self.seek += 1
            if root.right:
                dfs(root.right, level+1)
            if root.left:
                dfs(root.left, level+1)
        self.res = []
        self.seek = 0
        dfs(root, 0)
        return self.res
        

# the official explanation article points out that BFS will have a shorter queue/stack data structure
# for the worst case scenario where the tree is degenerate left skewed 
# ... but I'm not convinced (the article doesn't give a proof, and mapping this out seems to depend heavily on the presence of left-hand children and the direction of skew)
