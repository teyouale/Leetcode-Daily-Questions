class Solution:
    def isPossable(self,rate,piles,h):
        for i in piles:
            x = math.ceil(i/rate)
            h-=x
        if h <0:
            return False
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n= len(piles)
        left = 1
        right = max(piles) * math.ceil(n/h) 
        res = float('inf')
        while left<=right:
            mid = (left+right)//2
            
            current = self.isPossable(mid,piles,h)
            if current:
                right = mid-1
                res = mid
            else:
                left = mid+1
        return res