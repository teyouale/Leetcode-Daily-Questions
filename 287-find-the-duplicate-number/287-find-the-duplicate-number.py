class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = n -1
        res = n
        while l <= r:
            mid = l + (r-l)//2
            count = len([i for i in nums if i <= mid])
            if mid < count:
                res = mid
                r = mid -1
            else:
                l = mid + 1 
        return res
    
