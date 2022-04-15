from collections import Counter
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        root = [i for i in range(row*col)]
        ans = defaultdict(int)
        
        def encode(x,y):
            return x*col + y 
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX
                
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for nx, ny in {(0, 1), (1, 0)}:
                        tx, ty = i + nx, j + ny
                        if 0 <= tx < row and 0 <= ty < col and grid[tx][ty] == 1:
                            union(encode(i,j), encode(tx,ty))
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = find(encode(i,j))
                    ans[temp]+=1
                
        return max(ans.values()) if ans else 0
