"""
approach:
    brute force: gets a TLE
        simply sum the regions requested by iterating over the array
    
    below was my thought process for the caching solution marked Does Not Work
    see the Rectangular Caching and Row Caching for working caching solutions
    Caching: cache sums of already-visited regions
        we can do this because multiple calls are made to the same instance of NumMatrix
        in its simplest form 
            if we have already computed part of a range, reuse the sum from that part
            compute the new part and also store that sum so we can reuse it
        more comprehensive form 
            in a similar way, if we have already summed a larger area than the one we want,
            we can subtract the portion that we don't want from the existing sum
            
    Row Caching:
        make a DP matrix with the cumulative sums, row-wise (i.e. sum *along* the columns)
        compute the sum by computing dp[col2] - dp[col1] for each row in the requested range
    
    Rectangular Caching:
        make a DP matrix where each cell holds the sum of the rectangular area
            drawn from 0 to that cell (call 0 origin)
        to compute the sum of a region, fetch 4 areas:
            1) the sum from origin to the lower right hand corner at row2, col2
            2) the sum from origin to the upper right hand corner at row1, col2
            3) the sum from origin to the lower left hand corner at row2, col1
            4) the sum from origin to the upper left hand corner at row1, col1
        draw this out - it becomes clear
        the sum can be computed by: sum = 1 - 2 - 3 + 4
        alternatively, think of it as:
            sum = total_too_big_area - rectangle_above_range - rectangle_left_of_range + rectangle_that_we_subtracted_twice
        because 2 and 3 overlap on region 4, we need to add region 4 back in to break even
"""


# Rectangular caching (i.e. each cell should represent the rectangular sum from 0 to that cell)
# T: O(2*n*m) precompute time - 2 passes over the matrix (could call this simply n*m)
# T: O(1) summation compute time
# S: O(n*m) for the dp matrix
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        dp = self.dp
        # compute the rectangular cache by row-caching the matrix, then column-caching the row cache
        for i in range(len(matrix)):
            # row-wise caching pass
            for j in range(len(matrix[0])): 
                dp[i+1][j+1] = dp[i+1][j] + matrix[i][j] # +1 because first col is zero
            # column-wise caching pass
            for j in range(len(matrix[0])):
                dp[i+1][j+1] += dp[i][j+1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # since we have the rectangular cache, we can compute the sum by 
        # sum = larger - above - left + overlap
        # see explanation in comment block at the top of the file
        dp = self.dp
        larger  = dp[row2+1][col2+1]
        above   = dp[row1][col2+1]
        left    = dp[row2+1][col1]
        overlap = dp[row1][col1]
        
        rangeSum = larger - above - left + overlap
        return rangeSum
        
        
# Row Caching
# T: O(m*n) rows * columns precompute time
# T: O(r) summation compute time, where r is the number of rows in the range requested
# S: O(n*m) for the dp matrix
class __NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*(len(matrix[0])+1) for i in range(len(matrix))] # will hold cumulative sums row-wise (row caching) | the + 1 is so that the first column can hold zeroes
        # precompute dp matrix
        # holds cumulative sums increasing along the row, i.e. for each row, col1 holds col1, col2 holds col1+col2, col3 holds col1+col2+col3 where each reference to col refers to the input matrix
        for i in range(len(matrix)):
            # first col is zeros, because "sum col1 to col5" must be expressed as col5 cumulative sum minus col1 cumulative sum
            for j in range(len(matrix[0])): 
                self.dp[i][j+1] = self.dp[i][j] + matrix[i][j] # +1 because first col is zero

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summy = 0
        for i in range(row1, row2+1):
            summy += self.dp[i][col2+1] - self.dp[i][col1]
        return summy
        

# Dynamic programming, sorta - doesn't work, bad design
# T: O(n*cache size) varies based on how ideal the calls are relative to caching
# S: O(good god)  - scales with # of function calls
class __NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = {} # key will be tuple(row1, col1, row2, col2) and value will be sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        precomputed = self.getLargestOverlap(row1, col1, row2, col2)
        if precomputed == (): # didn't find a sum we can use
            summy = 0
            for i in range(row1, row2+1):
                for j in range(col1, col2+1):
                    summy += self.matrix[i][j]
            self.dp[(row1, col1, row2, col2)] = summy
            return summy
        else:
            summy = 0
            dpRowSpan = range(precomputed[0], precomputed[2]+1)
            dpColSpan = range(precomputed[1], precomputed[3]+1)
            for i in range(row1, row2+1):
                for j in range(col1, col2+1):
                    summy += self.matrix[i][j] if i not in dpRowSpan and j not in dpColSpan else 0
            summy += self.dp[precomputed]            
            self.dp[(row1, col1, row2, col2)] = summy
            return summy
            
    
    def getLargestOverlap(self, row1: int, col1: int, row2: int, col2: int) -> List[int]:
        lr1, lr2, lc1, lc2 = -1, -1, -1, -1
        area = 0
        # for each dp element, compute the overlap
        for r1, c1, r2, c2 in self.dp:
            if r1 >= row1 and r2 <= row2: 
                if c1 >= col1 and c2 <= col2:
                    # then we found a dp sum region entirely within our desired region
                    newArea = (r2-r1)*(c2-c1)
                    if newArea > area:
                        lr1, lr2, lc1, lc2 = r1, r2, c1, c2
                        area = newArea
        # if we found a suitable area, return its bounds
        return (lr1, lc1, lr2, lc2) if area > 0 else ()

        
        
# Brute force - gets TLE
# O(n) where in is the number of cells in the summation request
# O(1)
class __NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summy = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                summy += self.matrix[i][j]
        return summy


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
