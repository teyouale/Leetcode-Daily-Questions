class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtracking(r,cols,posD,negD,board):
            if n == r:
                copy = []
                for i in board:
                    copy.append(''.join(i))
                res.append(list(copy))
                return
            for c in range(n):
                if c in cols or (r+c) in posD  or (r-c) in negD:
                    continue
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                
                curr = ["."]*n
                curr[c]="Q"

                board.append(curr)
                
                backtracking(r+1,cols,posD,negD,board)

                board.pop()
                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                
                
            
        backtracking(0,set(),set(),set(),[])
        return res
            