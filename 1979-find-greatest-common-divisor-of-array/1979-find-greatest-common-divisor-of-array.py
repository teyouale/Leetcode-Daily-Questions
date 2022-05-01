class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)

        if  min_ == max_ :
            return min_
        
        res = 1
        
        for i in range(1,min_+1):
            if min_%i == 0 and max_%i == 0:
                res = i
        return res