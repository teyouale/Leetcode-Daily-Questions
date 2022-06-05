class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtracking(r,cols,posD,negD):
            nonlocal count
            if n == r:
                count+=1
                return 
            for c in range(n):
                if c in cols or (r+c) in posD  or (r-c) in negD:
                    continue
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                
                backtracking(r+1,cols,posD,negD)
                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                
                
        count = 0
        backtracking(0,set(),set(),set())
        
        return count
            