class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            count = 0
            curr = nums[i]
            for j in range(i,n):
                if curr < nums[j]:
                    count = max(dp[j],count) 
            dp[i] = count +1
        return max(dp)