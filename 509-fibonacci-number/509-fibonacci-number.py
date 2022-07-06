class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(None)
        def recc(n):
            if n ==0:
                return 0
            if n ==1:
                return 1
            return recc(n-1) + recc(n-2)
        
        return recc(n)