class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        n =  max(nums)
        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = max(counter[i]*i+dp[i-2],dp[i-1])
        return dp[-1]