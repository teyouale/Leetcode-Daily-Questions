class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res =dp = 1
        for i in range(len(prices)-2,-1,-1):
            if prices[i] == prices[i+1]+1:
                dp+=1
            else:
                dp=1
            res+=dp
        return res