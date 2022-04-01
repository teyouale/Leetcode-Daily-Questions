class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        zeroCount = 0
        onesCount = 0
        l = 0
        for r in range(len(nums)):
            if nums[r]:onesCount+=1
            else:zeroCount+=1
            while zeroCount > k and l<=r:
                if nums[l]:onesCount-=1
                else:zeroCount-=1
                l+=1
            res = max(res,r-l+1)
        return res