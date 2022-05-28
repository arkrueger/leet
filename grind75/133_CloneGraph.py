
"""
thoughts:
    could BFS work for this?
        treat each node as if it's a node in a n-ary tree
        store a list of visited nodes (node.val is unique for each node)
        
    
    
approach:
    BFS:
        standard bfs on the existing graph using a deque
        when we connect graph nodes, we need to have references to their neighbors in the new graph
            let's store these references in a dictionary with node value as the key (it's guaranteed unique)
        we can also use this dict to prevent infinite loop traversing over the existing graph
            (it serves as a log of which nodes we already visited)
        then do a second pass on BFS to connect the nodes to each other (we know where they are thanks to the first dict) - we'll need a second dict here to track which ones have already been connected so that we don't loop forever
        
    BFS: from the forum
        slight improvement on the BFS solution above
        instead of having 2 dicts, use just one
        no need to traverse twice
        here's how it works:
            create a dict of visited nodes
            do a breadth first search with a deque
                for each node popped by the deque, check if the node was already visited
                if it was not yet visited,
                    clone the node
                    add its neighbors (if a neighbor does not yet exist, create it and append it to the deque)
                        (if the neighbor does exist, look it up by keyvalue in the dict and link it)
            return the first cloned node
        a better explanation:
            start the deque with the given node
            start the visited (clones) dict with the given node's clone
            do the BFS:
                this is done in a way that means any popped deque item is guaranteed to exist in the visited dict
                    so use the visited dict to reference the current node's clone
                look at the current node's clone's neighbors - if any don't exist, clone them and add them to visited dict (this is better called clones dict but I'm keeping nomenclature consistent)
                only append new neighbors (nodes that were just now created) to the deque
                -> base case (deque runs empty) happens when we run out of undiscovered neighbors (i.e. we don't have any neighbors whose nodes still need to be created)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# BFS with 1 pass - using one dict to track which nodes we visited
# T: O(v+e)
# S: O(v)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        from collections import deque
        # set up deque and dict
        copies = {}
        copies[node.val] = Node(node.val, []) # initialize copies with the given node's copy
        q = deque([node])
        while q:
            n = q.popleft()
            c = copies[n.val] # current node copy
            for b in n.neighbors:
                if b.val not in copies: # if the neighbor doesn't exist, create it and dict it
                    copies[b.val] = Node(b.val, [])
                    # the deque append sort of makes a base case, we stop appending when all neighbor clones exist
                    q.append(b) # append original neighbor to the deque so that we visit it in our BFS
                c.neighbors.append(copies[b.val]) # add the neighbor to the new clone node
        return copies[node.val] # look up the given node's copy and return it


# BFS with 2 passes - using two dicts to track which nodes we already visited on each pass
# T: O(2*(v+e)) vertices plus edges, because we visit vertices and connect them via edges (link neighbors)
# S: O(2v)  vertices (two separate dicts for vertices)
class __Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        from collections import deque
        created = {} # keep track of nodes we have visited so they are processed only once
        connected = {} # keep track of which nodes we visited on the second traversal for the same reason
        q = deque([node])
        # first, use the deque to create all of the nodes
        while q:
            n = q.popleft()
            if n.val not in created:
                created[n.val] = Node(n.val, [])
                for nb in n.neighbors:
                    q.append(nb)
        # then, do the same thing again to make the connections
        # (we know where the connections live on the new graph thanks to the created dict)
        q = deque([node])
        while q:
            n = q.popleft()
            if n.val not in connected:
                connected[n.val] = 1 # we don't need to store the node object, just mark the key as completed
                for nb in n.neighbors:
                    # look up the neighbors of the current original node
                    # look up the node copy in the created dict, as well as the copies of the orig node neighbors
                    # add the copies as neighbors of the copy (elf on a shelf)
                    created[n.val].neighbors.append(created[nb.val])
                    q.append(nb)
        return created[node.val]
    
    # for graph viz
    def printGraph(self, node: 'Node') -> None:
        q = deque([node])
        # first, use the deque to create all of the nodes
        created = {}
        res = []
        while q:
            n = q.popleft()
            if n.val not in created:
                created[n.val] = Node(n.val)
                for nb in n.neighbors:
                    q.append(nb)
                    res.append([n.val, nb.val])
        print(res)
            
        
        
        
        
