class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a,b = s.split(':')
        
        startRow = ord(a[0])
        endRow = ord(b[0])
        
        startCol = int(a[1])
        endCol = int(b[1])
        res= []
        for i in range(startRow,endRow+1):
            for j in range(startCol,endCol+1):
                res.append(chr(i)+str(j))
        return res