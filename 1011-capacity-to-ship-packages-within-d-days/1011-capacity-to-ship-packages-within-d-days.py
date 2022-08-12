class Solution:
    def isPossible(self,current,weights,days):
            temp = 0
            days-=1
            for i in weights:
                if temp+i <= current:
                    temp+=i
                else:
                    days-= 1
                    temp = i
            if days < 0:
                    return False
            return True
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sum_ = sum(weights)
        
        left = max(weights)
        right = sum_
        
        res = sum_
        while left <= right:
            mid = (left+right)//2
            if self.isPossible(mid,weights,days):
                right = mid-1
                res= mid
            else:
                left = mid +1
        return res