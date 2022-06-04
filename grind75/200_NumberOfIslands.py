"""
approach:
    
    stack DFS:
        iterate row/col through the array
        when we encounter a 1, begin a DFS to find the extent of the island
            we could make another matrix to mark "visited"
            but the problem doesn't ask us to preserve the matrix so we'll just "sink" the islands
            we sink the island by turning all connected 1's to 0's
            after the island is sunk, increase the island counter and continue iterating on the matrix
            because we sunk the island, we will not double-count it as we iterate over remaining cells
    
    recursive DFS:
        just like above, but use recursive stack instead of a list stack
    
    deque BFS:
        same ol' deal   
    
notes on the Solution section:
    other approaches include:
        - Union Find: traverse horizontally and vertically to find connected pieces
"""

# BFS - deque
# T: O(n*m + a) where a is the total island area
# S: O(a) for the deque space
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        q = deque()
        m, n = len(grid), len(grid[0])
        islandCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q.append([i,j])
                    while q:
                        row, col = q.popleft()
                        if grid[row][col] == '1':
                            # append neighbors if coords are valid
                            dirs = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
                            for d in dirs:
                                if d[0] >= 0 and d[0] < m and d[1] >= 0 and d[1] < n:
                                    q.append([d[0], d[1]])
                            grid[row][col] = '0'
                    islandCount += 1
        return islandCount

# DFS - recursive
# T: O(n*m + a) where a is the total island area
# S: O(a) recursive space
class __Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islandCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.helper(grid, i, j)
                    islandCount += 1
        return islandCount
    
    # recursive helper func
    def helper(self, grid: List[List[str]], row, col) -> str:
        m, n = len(grid), len(grid[0])
        if grid[row][col] == '1':
            grid[row][col] = 0 # sink the current cell
            # recurse on its neighbors
            dirs = [[row+1,col],[row-1,col],[row,col+1],[row,col-1]] # updownrightleft
            for d in dirs:
                if (d[0] >= 0 and d[0] < m) and (d[1] >= 0 and d[1] < n):
                    self.helper(grid, d[0], d[1]) # recurse on neighbors if valid coords
            

# DFS - stack
# T: O(n*m + a) where a is the total island area
# S: O(a) stack space
class __Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        m, n = len(grid), len(grid[0])
        islandCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # if we find a 1, use DFS to sink the island and increase the island counter
                    stack.append([i,j])
                    while stack:
                        row, col = stack.pop()
                        # if current cell is 1, then check its neighbors
                        if grid[row][col] == '1':
                            dirs = [[row+1,col],[row-1,col],[row,col+1],[row,col-1]] # updownrightleft
                            for d in dirs:
                                if (d[0] >= 0 and d[0] < m) and (d[1] >= 0 and d[1] < n):
                                    stack.append((d[0],d[1])) # append neighbors if valid coords
                        # sink current cell
                        grid[row][col] = '0'
                    islandCount += 1
        return islandCount
                        
