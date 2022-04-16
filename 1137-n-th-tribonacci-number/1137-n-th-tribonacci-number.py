class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 =1
        t2=1
        current = 0
        if n == 1 or n==2:
            return 1
        for i in range(3,n+1):
            current =t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = current
        return current