"""
thinking:
    hearkens back to the rotten orange problem
    rotten orange solution goes like:
        iterate through the array and queue up rotten orange cells for BFS
        each cycle, pop all of the existing queue items
            modify the neighbors if applicable (in bounds and according to problem rules)
            append the modified neighbors' cells to the deque so that we can see them next pass

approach:
    
    round-by-round BFS:
        use the rotten-oranges approach
        iterate through the grid and add all the gates to a deque
        then,
        while the deque is not empty, popleft
            for each cell popped, check its neighbors
                if the neighbor value < current cell
                    then do nothing
                otherwise 
                    set the neighbor cell to current cell + 1
                    append the neighbor cell to the deque
        with this approach, any empty cells that are cut off from gates will remain INF, which we want
        
        IMPROVEMENT
            we actually don't need to check if the neighbor already has a lower distance than what we can offer
            all we need to do is check if it is less than INF (i.e. has been visited and received a distance)
            if it has been filled via BFS before the current cycle got to it, then logically it MUST be a lower distance because all paths are moving at the same speed

"""

# round-by-round BFS
# T: O(n) n is grid size 
# S: O(1) we are not creating any new data structures
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        from collections import deque
        empty = 2147483647 # denotes an empty room
        m, n = len(rooms), len(rooms[0])
        q = deque()
        # fill the deque with the gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i,j])
        # BFS traversal
        dirs = [[1,0],[0,1],[-1,0],[0,-1]] # cardinal directions
        while q:
            r, c = q.popleft() # row and col
            # distance to nearest gate, will remain 0 if current room is a gate
            distance = rooms[r][c] if rooms[r][c] > 0 else 0
            # examine current room's neighbors
            for d in dirs:
                nr, nc = r+d[0], c+d[1]
                # if the index is valid and it's not a wall, gate, or already visited
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == empty: 
                    # then give the neighbor that distance and append the neighbor to queue
                    rooms[nr][nc] = distance + 1
                    q.append([nr,nc])
                    # if the neighbor already has a distance,
                    # then stop BFS'ing in that direction 
                    
    # more concisely without the comments
    def __wallsAndGates(self, rooms: List[List[int]]) -> None:
        from collections import deque
        empty = 2147483647 
        m, n = len(rooms), len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i,j])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            r, c = q.popleft()
            distance = rooms[r][c] if rooms[r][c] > 0 else 0
            for d in dirs:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == empty: 
                    rooms[nr][nc] = distance + 1
                    q.append([nr,nc])


