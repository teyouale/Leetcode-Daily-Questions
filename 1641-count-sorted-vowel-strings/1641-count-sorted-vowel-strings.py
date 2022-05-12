class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0,1,2,3,4,5]
        for i in range(1,n):
            for j in range(1,6):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
            