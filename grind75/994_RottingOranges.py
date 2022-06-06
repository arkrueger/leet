"""
thinking:
    looking at the test cases
        if we have any 4-directional fresh-orange "islands" 
            (one or more fresh oranges not connected to a rotten orange)
            -> we probably want to start with the fresh oranges and not the rotten ones?
            -> no, let's still start with the rotted oranges
    this is similar to the "water and islands 1's and 0's question"
    we should take a similar approach

approach:
    *** THIS solution will not work because it assumes no rotting paths will meet in the middle
    *** in other words what happens if we have two rotten oranges across from each other on the island?
    *** this solution fundamentally does not account for that
    DFS with island sinking
        iterate through the array to find the rotten oranges
            if we find a rotten orange, rot all of its neighbors and count how many "minutes" it took
            store the max # of minutes that any given island took to sink as we find new islands
        iterate through the array again searching for fresh oranges
            if we see even a single fresh orange, return -1 because it was a fresh orange island
            if we see no fresh oranges, return the number of minutes that any island took to rot
        thoughts:
            on the "1/0 island" problem we didn't have to count how long the islands took to sink
            how do we do this here?
                could pass a "rank" to the recursive DFS call (or store value in stack if iterative)
                to track how deep we are in the tree
                then add this up on return (if recursive)
                    or preserve the max rank (num of minutes) if iterative
            let's edit the matrix directly and use -1 to indicate a visited & rotted cell (to minimize calls to the rot helper function)
            
    ***THIS WORKS***
    Correct approach using BFS: (you could use DFS, but BFS is cleaner to code for this purpose)
        we have to work through the array, "minute" by "minute"
        fresh oranges will rot in minute-based cohorts
        
        iterate over the grid
            count the fresh oranges
            collect the rotten oranges, add them to a queue
                
        now loop while rotten queue is not empty and fresh count > 0
            iterate over the BFS queue to current length (don't cover elements that we add during this loop)
            rot the cell's neighbors and add them to the queue to be processed on the next iteration of the *outer* loop
            decrease the fresh orange count accordingly
            
"""
# concurrent BFS (rot the oranges in place, 1 cycle = 1 minute)
# T: O(m*n + o)  where m*n is grid size for precompute time, o is num of oranges for rot time
# note: always o < m*n, so this simplifies to T: O(grid size)
# S: O(s) where s is the surface oranges (i.e. the rotten queue)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        
        # count up all the fresh oranges, and add the rotten oranges' coordinates to a deque
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 1:
                    fresh += 1; continue
                if grid[r][c] == 2:
                    rotten.append([r,c])
        
        # keep going until we have rotted all rot-able oranges
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] # 4 directions
        minutes = 0
        while rotten and fresh > 0:
            minutes += 1
            # iterate over the current elements in rotten (but not the elements that we add here)
            # this is why we use a deque and not a stack, because we need to pop/append on opposing side
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                # rot each fresh neighbor and add to the queue, decrement fresh count
                for d in dirs: # 4-directionally
                    nr, nc = row+d[0], col+d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1: # check if index is valid
                        grid[nr][nc] = 2 # rot
                        rotten.append([nr, nc]) # add to rotten queue
                        fresh -= 1 # one less fresh orange now... 99 bottles of beer on the wall
        return minutes if fresh == 0 else -1
            
            


"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass
    
    # helper function to rot the oranges -> returns num of minutes the given island took
    def rot(self, grid: List[List[int]], row: int, col: int) -> int:
        stack = [[row, col, minute]]
        dirs = [0,1,0,-1,0] # directions to DFS
        while stack:
            row, col, minute = stack.pop()
            if grid[row][col] < 1:
                break # move forward on the stack, cell is either empty or alread visited and rotted
            if grid[row][col] == 1:
                grid[row][col] = -1 # mark as visited
            if grid[row][col] == 2
"""
