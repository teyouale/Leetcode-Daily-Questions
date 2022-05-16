class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
                
        return self.bfs(grid)
            
    def bfs(self, grid):
        dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        queue = [(0, 0, 1)]         # row, col, cost

        while queue:
            size = len(queue)
            
            for _ in range(size):
                row, col, cost = queue.pop(0)
                
                if row == len(grid) - 1 and col == len(grid) - 1:      
                    return cost
                if grid[row][col] == 1:                                
                    continue
                
                grid[row][col] = 1
                
                for r, c in dirs:
                    nrow, ncol = row + r, col + c
                    
                    if self.isValidCell(grid, nrow, ncol) and grid[nrow][ncol] == 0:
                        queue.append((nrow, ncol, cost + 1))
                
        return -1
        
    def isValidCell(self, grid, row, col):
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])