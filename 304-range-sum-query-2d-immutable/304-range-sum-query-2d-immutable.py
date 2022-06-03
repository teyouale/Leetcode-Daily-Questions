class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW = len(matrix)
        COL = len(matrix[0])
        self.prefixSum = [[0] * (COL+1) for r in range(ROW+1)]  
        for r,m in enumerate(matrix):
            temp = 0
            for c,i in enumerate(m):
                above = self.prefixSum[r][c+1]
                temp += i
                self.prefixSum[r+1][c+1] = above+temp
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        res = 0
        end = self.prefixSum[r2+1][c2+1]
        above = self.prefixSum[r1][c2+1]
        side = self.prefixSum[r2+1][c1]
        intersection = self.prefixSum[r1][c1]
        return end+intersection - side - above


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)'
