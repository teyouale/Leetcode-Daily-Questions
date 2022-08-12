class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        
        while True:
            mid = (l+r)//2
            current = (mid)*mid
            next_ = (mid+1) * (mid+1)
            if current <= x < next_ :
                return mid
            if current < x:
                l  = mid+1
            else: r = mid -1
        