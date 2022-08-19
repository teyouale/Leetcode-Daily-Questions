class Solution:
    def isPossiable(self,current,piles,h):
        count = 0
        for i in piles:
            count+=math.ceil(i/current)
        return count <=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 1
        right = max(piles) * math.ceil(n/h) 
        best = right
        while left <= right:
            mid = left + (right-left)//2
            if self.isPossiable(mid,piles,h):
                right = mid -1
                best = mid
            else:
                left = mid + 1
        return best