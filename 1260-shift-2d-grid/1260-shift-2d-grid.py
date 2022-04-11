class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r= len(grid)
        c=len(grid[0])
        
        res =[[0] *c for i in range(r)]
        for i in range(r):
            for j in range(c):
                odp = ((i*c + j) + k) % (r*c)
                nr ,nc  = odp//c ,odp%c
                res[nr][nc] = grid[i][j]
        return res