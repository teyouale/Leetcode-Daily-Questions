class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        res = 0
        for i,j in boxTypes:
            if truckSize < 0:break
            res+=(min(i,truckSize)*j)
            truckSize-=i
        return res
                
