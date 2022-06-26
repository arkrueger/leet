"""
thinking:
    
    robot needs to get from s to e
    can only make moves down or right
    s x x x x
    x x x x x
    x x x x e
    
    our "next move" space expands as we leave s and travel toward the diagonal
        contracts as we pass the diagonal
    other thoughts:
        as soon as we exhaust our right-moves, the only option is down (i.e. we don't actually need to explore)
        as soon as we exhaust our down-moves, the only option is right (same deal)
    
    if we were to approach this from a bottom up approach, we would start from our end cell (bottom left)
        at each stage, we identify candidate moves (left and up)
        actually, I don't know if this satisfies the definition of dynamic programming
        but if we use a depth first search, then when we reach a node that was already explored, there will be a result already computed for the potential paths downstream from it
             we can use this and avoid recomputing
    
    additional thoughts:
        if we're using BFS, to further improve space complexity it should be possible to forget about the dp matrix and use a DP array instead
        the DP array would represent the leading edge of the search, i.e. the current level
    
approach:

    breadth first search with DP:
        treat the matrix as a graph that begins on one end with the top left cell
            and ends with the bottom right
        graph, tree, all the same to me
        initialize a DP matrix size m*n to hold info about unique paths to reach that cell's parent
        initialize a queue to hold [i=0,j=0,paths=0] 
            where i,j are graph node coords and paths is the number of unique paths to reach the node
                    a quick aside, here's the secret algo sauce:
                        if we already visited the cell, we *do* want to increment the number of unique paths leading *to* that cell
                        *but* we do not want to add its children to the queue a second time, because that would be a false duplicate (i.e. we'd visit the children again and increase their unique path numbers, but it's not actually a unique path because we already visited those cells from the parent cell, make sense? on the other hand, it's totally fine to have duplicates in the queue when the duplicate cell is being reached from two different parents, i.e. from above and from left)
        while queue is not empty:
            popleft into i,j,paths
            is current node = target? *actually* we don't need to check this
                no -> is current node in DP matrix?
                    yes -> increment its path value in the DP matrix but do not append to queue
                    no  -> add [i+1,j,paths+1] and [i,j+1,paths+1] to queue
                        -> set dp[i][j] to the value of its parent
        exit when queue is empty
        each cell now contains the number of unique paths to it
        return dp[-1][-1] because it contains the number of unique paths to the target cell
        
"""

# BFS with DP
# T: O(v+e) v=vertices, or m*n | e=edges, or m*n (because there are m down-moves, and n right-moves)
# S: O(m*n+b) m*n for the DP matrix, b for the max number of nodes in a level (queue length)
class __Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from collections import deque
        queue = deque([[0,0,0,0]]) # starting coords for the node and its parent (ni,nj,pi,pj)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 # one unique path to the starting cell
        # build the path count
        while queue:
            i, j, pi, pj = queue.popleft()
            paths = dp[pi][pj]
            if dp[i][j] == 0 or i+j == 0: # then we have not visited this before, so search its children
                if i+1 < m: # if there is a next row, add the child below
                    queue.append([i+1,j,i,j])
                if j+1 < n: # if there is a next column, add the child right
                    queue.append([i,j+1,i,j])
            dp[i][j] += paths 
        # dp[-1][-1] contains double the unique paths to m, n
        return dp[-1][-1]//2
    
# the simpler way to do it is this:
# instead of breadth first search, simply build the solution row-wise
# what was the secret algo sauce from the solution above? : the unique paths to any cell are the unique paths to the cell above it plus the unique paths to the cell to the left of it
# since we move from left to right, we can even collapse the dp matrix to a 1d array
# i.e. dp[i][j-1] is equal to dp[j] if we iterate over dp for each row
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
