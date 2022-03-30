class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        mod = 10**9 + 7
        for i in range(1,n):
            # s = i+2
            s = (i)*2 + 1
            res = res * s * (i+1)

        return res % mod