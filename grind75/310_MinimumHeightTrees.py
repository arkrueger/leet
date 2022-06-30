"""
thinking:
    
    we probably want to build an adjacency graph with a hash map (dict)
    how do we identify the min height trees?    
    hmmm
    the only way we can identify max depth is by searching the tree?
    maybe not quite like that
    looking at the examples, the valid roots are those that have the shortest "furthest distance to another node" if that makes sense
    can we traverse the tree once and assign "distance to furthest node" values to each node?
        for simplicity start with a node that has only a single connection
        0, recurse on children (3)
        3, recurse on children not including parent (1,2,4), return longest distance found (parent will add this to their distance, and return that)
        when we encounter a dead end (no children aside from parent) return 1
        
        
        

approach:
    
    DFS:
        find an end node (one with only one connection)
        perform dfs from this node
            recursively add up the distance
                (i.e. when we encounter a node with no additional connections, don't recurse and instead just return 1)
                when we receive the value from the recursive call, return the recursive call + 1
                
        this should give us a map of the distances
        now we want to return a list of the nodes with the shortest distance

"""

# trim leaf nodes, official solution
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge cases
        if n <= 2:
            return [i for i in range(n)]
        
        # adjacency list
        adj = [set() for i in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        # find the leaves (these are nodes with only one connection)
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        # trim the leaves repeatedly until we have < 2 nodes remaining
        remainingCount = n
        while remainingCount > 2:
            remainingCount -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                newleaf = adj[leaf].pop() # remove the leaf
                adj[newleaf].remove(leaf) # remove the leafward connection
                if len(adj[newleaf]) == 1: # only add the neighbor if it's a leaf
                    new_leaves.append(newleaf)
            # set leaves to the new leaves for the next iteration
            leaves = new_leaves
        return leaves



# this might work in theory but my implementation is bad
class __Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build the adjacency list (cuts down on list search time)
        adj = {}
        for a,b in edges:
            adj[a] = adj.get(a, set()); adj[b] = adj.get(b, set())
            adj[a].add(b); adj[b].add(a)
        # assign "distance to furthest node" for each node
        dist = [0] * n
        visited = [False] * n
        def dfs(node):
            print(visited)
            if not visited[node]:
                visited[node] = True
                for n in adj[node]:
                    newDist = dfs(n)
                    print(newDist)
                    dist[node] = max(newDist, dist[node])
                return dist[node] + 1
            return dist[node]
        # find an edge node
        for n in adj:
            if len(adj[n]) == 1:
                startingNode = n
                break
        print(startingNode)
        dfs(startingNode)
        print(dist)
        return []
