class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp ={}
        def solve(r,c,left):
            if (r,c,left) in dp:
                return dp[(r,c,left)]
            if left < 0:return 0
            if r < 0 or r >= m or c < 0 or c >= n:return 1
            dp[(r,c,left)] =  solve(r-1, c, left - 1)+ solve(r+1, c, left - 1)+ solve(r, c-1, left - 1)+ solve(r, c+1, left - 1)
            return dp[(r,c,left)]
            
        return solve(startRow, startColumn, maxMove) % 1000000007
    
