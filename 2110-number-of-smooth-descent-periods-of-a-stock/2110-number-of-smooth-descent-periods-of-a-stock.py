class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        stack = []
        descents = 0
        for price in prices:
            if not stack or stack[-1] - price == 1:
                stack.append(price)
            else:
                n = len(stack)
                descents += (n*(n+1) // 2)
                stack = [price]
            n = len(stack)
        descents += (n*(n+1) // 2)
        return descents
            
            