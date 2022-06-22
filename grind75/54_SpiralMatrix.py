"""
thinking:
    
    edge cases - what if m | n == 1?
    will we handle empty matrices?
    we always start out at the top left (0,0)
    
    napkin sketch
        
        l, r, t, b - for left right top bottom
        l = t = 0
        b = len(matrix)-1 # bottom is the end of the rows
        r = len(matrix[0])-1 # right is the end of the cols
        
        loop to gather the spiral portions, alternating between:
            1. left->right (on top)
            2. top->bottom (on RHS)
            3. right->left (on bottom)
            4. bottom->top (on LHS)
        what does each straight length look like?
            1. l:r with t as initialized
            2. t:b with r as initialized
            3. r:l with b as initialized
            4. t++ then b:t 
            next iteration
            1. r-- then l:r 
            2. b-- then t:b 
            3. l++ then r:l 
            4. t++ then b:t
        exit cases:
            if t >= b
            if l >= r

approach:
    
    iterative with four pointers:
        T: O(m*n)
        S: O(1)
        vars:
            l, r, t, b - for left right top bottom
            l = t = 0
            b = len(matrix)-1 # bottom is the end of the rows
            r = len(matrix[0])-1 # right is the end of the cols
            res = [] # result
        iterate:
            exit cases:
                1.  l > r
                2.  t > b
            extend result with:             unless exit case:
                mat[t][l:r+1] then t++          1
                mat[t:b+1][r] then r--          2
                mat[b][r:l-1] then b--          1
                mat[b:t-1][l] then l++          2
                
    

"""

# iterative 4 pointer
# T: O(m*n) for the spiral traversal
# S: O(m*n) for the result list
class __Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import numpy as np
        matrix = np.array(matrix)
        l = t = 0
        b = len(matrix)-1
        r = len(matrix[0])-1
        res = []
        while True:
            if l <= r:
                res.extend(matrix[t,l:r+1])
                t += 1
            else: break
            if t <= b:
                res.extend(matrix[t:b+1,r])
                r -= 1
            else: break
            if l <= r:
                res.extend(matrix[b,r:(None if l-1 < 0 else l-1):-1])
                b -= 1
            else: break
            if t <= b:
                res.extend(matrix[b:(None if t-1 < 0 else t-1):-1,l])
                l += 1
            else: break
        # end of while loop
        return res
        

        
        
# another approach suggested in the forum
# much faster than the approach laden with if statements
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dir = 1 # directions 1: up 2: down
        i, j = 0, -1 # initialize j as -1 because we start by incrementing it
        res = []
        # two nested loops inside the while
        # each iteration alternates between "left->right, up->down" and "right->left, down->up"
        while m*n > 0: # m rows, n cols
            for _ in range(n):
                j += dir
                res.append(matrix[i][j])
            m -= 1 # decrement m because we consumed a row
            for _ in range(m):
                i += dir # remember i was preserved from last iteration, now we use the direction to move either up or down as appropriate
                res.append(matrix[i][j])
            n -= 1 # decrement n because we consumed a column
            dir *= -1 # alternate the direction
        return res
