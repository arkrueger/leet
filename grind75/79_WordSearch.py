"""
thinking:
    
    can't track back over the cells we already covered
    i.e. abcb must appear as abcb, we can't reuse the b after we visit it
    
    my inclination is to do backtracking BFS starting from one cell 
        use a visited matrix to avoid revisiting a cell
    do this for all cells

approach:

    backtracking DFS:
        iterate over the matrix and visit each cell
            each cell we visit will be a "starting cell"
            from each starting cell, do a DFS to build candidate words
                store each visited cell in the visited matrix
                how to "unwind" the visited matrix when we abandon a path?
                since it's DFS, probably best to use recursion and reset the current cell in the visited matrix after the function call returns
        T: O(m*n * 3^w)
            at worst we will visit each cell of the array
                from each cell, we begin a DFS that has a worst height of w (word length) and 4 children per node
                ->m*n (visit each starting cell)
                -> 3^w (DFS) (why not 4? because we won't check the cell we came from, it's marked as visited)
        S: O(m*n + w + w) m*n for the visited array, w for the wordSoFar, w for the recursive stack (we visit to a max depth of w)


"""

# recursive backtracking DFS
# T: O(m*n * 3^w) 
# S: O(m*n + w)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # recursive helper
        def search(i: int, j: int, wordSoFar: List[chr], visited: List[List[int]]) -> bool:
            # can't use already-visited cells
            wordSoFar.append(board[i][j])
            # check if the current letter is a match
            if wordSoFar[-1] == word[len(wordSoFar)-1]:
                # check if this was the last character we needed to match
                if len(wordSoFar) == len(word): 
                    return True # we found a match, propagate True back through the chain
            else: # if the current letter is not a match, backtrack (don't pursue this branch any further)
                return False
            # if the current letter was a match but we haven't built the full string, then
            # mark as visited and recurse on neighbors
            visited[i][j] = True
            dirs = [[1,0],[0,1],[-1,0],[0,-1]] # down right up left
            for row, col in dirs:
                row += i; col += j
                # if the up/down/right/left doesn't go out of bounds
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and not visited[row][col]:
                    if search(row, col, wordSoFar, visited):
                        return True
                    wordSoFar.pop() # unwind wordSoFar
                # reset visited for this cell only (i.e. "unwind" as we pop the recursive stack)
            visited[i][j] = False
            return False
        # main
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if search(i, j, [], visited):
                    return True
        # if we didn't find it in the list, return False
        return False
