class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res = float('inf')
        for i in range(len(timePoints)-1,-1,-1):
            HH,MM = map(int,timePoints[i].split(':'))
            HHC,MMC = map(int,timePoints[i-1].split(':'))
            HH*=60
            HHC*=60
            
            x = abs((HH+MM) - (HHC+MMC)) 
            y = abs((HH+MM) - (HHC+MMC)  + 1440) 
            res=min(res,x,y)
        return res