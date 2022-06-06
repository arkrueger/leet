"""
context:
    not trying to solve this problem, using it to understand how union finds work
    
approach:
    
    DFS:
        note: 
            each node is blind 
            (i.e. we only have edge info, so by looking at a node we do not know all of its connections)
            I think this means that we can't use a stack for the DFS 
                (b/c we don't know all of a node's children just by looking at one edge definition)
            therefore, I think we *do not* need a stack to perform the connection search
        consider each edge (u,v) in the order they are given in the input
        perform a dfs starting with u:
            if we see v in the dfs, that means there is an additional connection from u to v
            i.e. there is a cycle in the graph
        because there may be multiple edges that could be removed to nix the cycle, return the last one
        
        in clearer detail:
            we create a dict
                the keys will be node values
                each the values will be sets (containing all nodes reachable from that the key node)
                the sets will grow as we 
        
    union find:
        implement a disjoint union set class
        iterate through the edges and perform unions
        return the first edge that is already pointing to the same root (i.e. no union was performed)
        
"""

# Disjoint Set Union with ranking
# T: O(n) where n = number of vertices or edges
# S: O(n) the parent list and rank list are both size n
class DSU: # disjoint set union
    def __init__(self): 
        self.parent = [i for i in range(1001)] # problem statement says we have at most 1000 edges
        self.rank = [0] * 1001
    
    # helper function to recursively find any node's absolute root
    def find(self, x):
        parent = self.parent
        if parent[x] != x: # if x isn't its own parent (it isn't the root of a set)
            parent[x] = self.find(parent[x]) # return x's root (the ancestor who is its own parent)
        return parent[x]
    
    def union(self, x, y):
        parent, rank = self.parent, self.rank
        xroot, yroot = self.find(x), self.find(y)
        # if they have the same root, return false (no union was created, it already existed)
        if xroot == yroot:
            return False
        elif rank[xroot] < rank[yroot]: # if yroot ranks higher, make it xroot's root
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: # if xroot ranks higher, make it yroot's root
            parent[yroot] = xroot
        else: # if their ranks are equal, make xroot the root of yroot and increase xroot's rank
            parent[yroot] = xroot
            rank[xroot] += 1
        return True # if we actually performed a union
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for u,v in edges:
            if not dsu.union(u,v):
                return u,v



# DFS iterative
# T: O(n^2)
# S: O(n) stack space
class __Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(set)
        
        # iterative helper function to find cycles
        def dfs(source: int, target: int) -> bool:
            stack = [source]
            while stack:
                source = stack.pop()
                if source not in seen:
                    seen.add(source)
                    if source == target: 
                        return True
                    stack.extend([neighbor for neighbor in graph[source]])
            return False # if we visited all available nodes and didn't return True
        
        for u, v in edges:
            seen = set() # "was this evaluated by dfs as a source (u) node? if yes, then it is in seen"
            # b/c short circuit, dfs() won't be called until both u and v are in graph
            if u in graph and v in graph and dfs(u, v):
                return u,v
            graph[u].add(v) # really important note about these graph.add()'s below
            graph[v].add(u)
            """
            these can only be added to the graph AFTER running dfs(u,v) in the conditional above
            (and dfs(u,v) will only be run if both u and v are in the graph)
            the reason for this is:
                when we  run dfs, we are trying to see if we can reach v (target) from u 
                by traversing through u's OTHER neighbors, i.e. not 5
                we do this through the set of neighbors stored as a value in the graph dict
                    (and their neighbors)
                    and checking if we come across v (target) through this alternate route
                if u and v's DIRECT connection (i.e. running graph[u].add(v) and the reciprocal)
                    already existed in the graph dict, then we would always find v (target) 
                    through u's set (at graph[u]) because v is in that set
            that's why graph.add's are done after the "are these connected indirectly?" check
            """




# DFS recursive
# T: O(n^2) because we traverse down n nodes for each edge
# S: O(n) for the dict describing node neighbors
class __Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(set)
        
        # recursive helper function to see if we can get from node u to node v via other nodes
        # aka finds out of there is a cycle connecting u to v
        def dfs(source: int, target: int) -> bool: 
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(n, target) for n in graph[source])
        
        for u, v in edges:
            seen = set() # "was this evaluated by dfs as a source (u) node? if yes, then it is in seen"
            # b/c short circuit, dfs() won't be called until both u and v are in graph
            if u in graph and v in graph and dfs(u, v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)

            
            
            
            
            
            
            
