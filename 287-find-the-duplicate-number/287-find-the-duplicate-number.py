class Solution:
    def isPossable(self,current,nums):
        count = 0
        for i in nums:
            if i <= current:
                count+=1
        return count
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = n -1
        res = n
        while l <= r:
            mid = l + (r-l)//2
            
            if mid < self.isPossable(mid,nums):
                res = mid
                r = mid -1
            else:
                l = mid + 1 
        return res
    
