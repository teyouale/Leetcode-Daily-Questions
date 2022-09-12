class Solution:
    
    def isCap(self,cap,days,nums):
        temp = 0
        days-=1
        for i in nums:
            if temp+i <= cap:
                temp+=i
            else:
                days-= 1
                temp = i
            # print(temp,days)
        if days < 0:
                return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r =ans = sum(weights)
        while (l<r):
            mid = (l +r )//2
            pos = self.isCap(mid,days,weights)
            # print(pos,mid)
            if pos:
                r = mid 
                ans = mid
            else:
                l = mid+1
        return ans