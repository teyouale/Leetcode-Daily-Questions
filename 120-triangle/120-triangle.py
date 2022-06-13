class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[-1]
        row = len(triangle)
        for i in reversed(triangle[:-1]):
            currRow= []
            for k,v in enumerate(i):
                currRow.append(min(res[k]+v,res[k+1]+v))
            res = currRow[:]
        return res[0]