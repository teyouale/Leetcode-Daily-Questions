class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for i in range(1,amount+1):
            temp = [amount+1]
            for coin in coins:
                x = i - coin
                if x > -1:
                    temp.append(1+dp[x])
            dp.append(min(temp))
        if dp[-1] == amount+1:
            return -1
        return dp[-1]        