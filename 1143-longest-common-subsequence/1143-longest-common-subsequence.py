class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        xm = len(s1)
        xn = len(s2)
        res = 0
        @lru_cache(None)
        def recc(m,n):
            nonlocal res
            if xm == m or xn == n:
                return 0
            if s1[m] == s2[n]:
                return 1+recc(m+1,n+1)
            else:
                return max(recc(m+1,n),recc(m,n+1))
        return recc(0,0)
