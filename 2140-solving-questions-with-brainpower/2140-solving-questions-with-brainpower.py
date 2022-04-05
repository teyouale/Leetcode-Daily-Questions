class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            cp,ck = questions[i]
            if (ck + i+1) < n: dp[i] = max(cp+dp[ck+i+1],dp[i+1])
            else: dp[i] = max(cp + dp[n],dp[i+1])
        return dp[0]