class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        zeroCount = 0
        onesCount = 0
        l = 0
        for r in range(len(nums)):
            if not nums[r]:zeroCount+=1
            while zeroCount > k and l<=r:
                if not nums[l]:zeroCount-=1
                l+=1
            res = max(res,r-l+1)
        return res