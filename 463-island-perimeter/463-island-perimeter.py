class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visted = set()
        res = 0
        def dfs(r,c):
            nonlocal res
            nonlocal visted
            if (r,c) in visted:
                    return
            if r < 0 or c < 0 or r > row-1 or c >col-1:
                res+=1
                return 
            if grid[r][c] == 0:
                res+=1
                return 
                
            visted.add((r,c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x,y in directions:
                dfs(r+x,c+y)
            return 
        # dfs(0,0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = dfs(i, j)
        return res