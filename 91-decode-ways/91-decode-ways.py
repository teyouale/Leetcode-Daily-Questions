class Solution:
    # def convert(self,curr):
        # return ord
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp  =[0]*(n+2)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            if s[i] != '0':
                curr = int(s[i:i+2])
                if 1<=curr<=26:
                    # if s[i:i+2]
                    dp[i]= dp[i+1] + dp[i+2]
                else:
                    dp[i]=dp[i+1]
            else:
                dp[i]=0
        return dp[0]