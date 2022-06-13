class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[-1]
        row = len(triangle)
        for i in range(row-2,-1,-1):
            currRow= []
            for k,v in enumerate(triangle[i]):
                currRow.append(min(res[k]+v,res[k+1]+v))
            res = currRow[:]
        return res[0]