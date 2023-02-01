class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """        col          row
        1,2,3     5,7,9         3,6,5
        4,5,6     12,15,18      9,15,11
        7,8,9     11,13,15      15,24,17

        6,6,6    12
        15,15,15
        24,24,24

                          row               col
        1, 2, 3, 4       6, 10,10, 9       15,18,21,24
        5, 6, 7, 8       18,26,26,21
        9, 10,11,12
        13,14,15,16

        5    14,16,18
        13
        21
        """        
        inbound = lambda x,y: 0<= x < m and 0<= y <n
        m = len(mat)
        n = len(mat[0])
        cols = [ [0]*n for _ in range(m)]
        res = [ [0]*n  for _ in range(m)]
        def columnHelper(row,col):
            postiveCol = 0
            left = k
            currRow =  row + 1
            while left > 0 and inbound(currRow,col):
                postiveCol += mat[currRow][col]
                currRow+=1
                left -=1
            
            negativeCol = 0
            left = k
            currRow =  row - 1
            while left > 0 and inbound(currRow,col):
                negativeCol += mat[currRow][col]
                currRow-=1
                left -=1
            return negativeCol + postiveCol + mat[row][col]

        def rowHelper(row,col):
            postiveRow = 0
            left = k
            currCol =  col + 1
            while left > 0 and inbound(row,currCol):
                postiveRow += cols[row][currCol]
                currCol+=1
                left -=1

            negativeRow = 0
            left = k
            currCol =  col - 1
            while left > 0 and inbound(row,currCol):
                negativeRow += cols[row][currCol]
                currCol-=1
                left -=1
            return postiveRow + negativeRow + cols[row][col] 

        for row in range(m):
            for col in range(n):
                cols[row][col] = columnHelper(row,col)
        for row in range(m):
            for col in range(n):
                res[row][col] = rowHelper(row,col)
        return res
                
