### GRIND 75 SECOND PASS ###

"""
approach:
    recursive:
        keep track of the original color (this helps us to track which cells are destined for flood fill vs were already the new color because we will recurse on cells we already visited if they are adjacent to the current cell)
        ^ you could call that DP, maybe? it's more space efficient than creating an extra matrix of "visited cells"
        base case: when we run the function call on a cell that is not original color -> return image
        otherwise, if current cell is original color, then change it to the new color
            recurse on all valid neighbors (stay in bounds of the image matrix)
        return the image when done (we modified the image directly)
        
    breadth-first search BFS:
        start from given pixel, consider a pixel's "children" as the cardinal neighbors
        store the original color
        add the pixel to a deque
        loop while the deque has items:
            popleft
            if pixel == original color 
                change it to new color
                append its "children" (check row/col validity first) to the deque
            if not, do nothing
        return image
    
    depth-first search DFS:
        same thing as the BFS, but pop and append with a stack instead of a deque
"""

# DFS
# T: O(?)
# S: O(?)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        origColor = image[sr][sc]
        # don't do anything if the new color isn't different
        if newColor == origColor:
            return image
        m, n = len(image), len(image[0])
        q = [(image[sr][sc], sr, sc)]
        dirs = [(-1,0), (1,0), (0, -1), (0, 1)] # up, down, left, right
        while q:
            pixel, r, c = q.pop()
            if pixel == origColor:
                image[r][c] = newColor
                for d in dirs:
                    newR = r+d[0]
                    newC = c+d[1]
                    if (newR < m and newR >= 0) and (newC < n and newC >= 0): # don't recurse out of bounds of the image
                        q.append((image[newR][newC], newR, newC))
        return image

# BFS
# T: O(?)
# S: O(?)
class __Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        origColor = image[sr][sc]
        # don't do anything if the new color isn't different
        if newColor == origColor:
            return image
        m, n = len(image), len(image[0])
        q = deque([(image[sr][sc], sr, sc)])
        dirs = [(-1,0), (1,0), (0, -1), (0, 1)] # up, down, left, right
        while q:
            pixel, r, c = q.popleft()
            if pixel == origColor:
                image[r][c] = newColor
                for d in dirs:
                    newR = r+d[0]
                    newC = c+d[1]
                    if (newR < m and newR >= 0) and (newC < n and newC >= 0): # don't recurse out of bounds of the image
                        q.append((image[newR][newC], newR, newC))
        return image        

# recursive
# not sure about the time and space complexity
class __Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, origColor: int=-1) -> List[List[int]]:
        # renaming for easier keyboarding
        r, c = sr, sc
        m, n = len(image), len(image[0])
        if origColor == -1:
            origColor = image[r][c]
        dirs = [(-1,0), (1,0), (0, -1), (0, 1)] # up, down, left, right
        # base case: the pixel is already the new color
        if image[r][c] != origColor:
            return image
        # if current cell color is part of the flood fill region (is origColor), change color and recurse on neighbors
        if image[r][c] == origColor:
            image[r][c] = newColor
            for d in dirs:
                newR = r+d[0]
                newC = c+d[1]
                if (newR < m and newR >= 0) and (newC < n and newC >= 0): # don't recurse out of bounds of the image
                    self.floodFill(image, newR, newC, newColor, origColor)
        return image