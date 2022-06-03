class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = []
        
        for m in matrix:
            temp = [0]
            for x in m:
                temp.append(temp[-1]+x)
            self.prefixSum.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1,row2+1):
            res+=self.prefixSum[i][col2+1]- self.prefixSum[i][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)'
