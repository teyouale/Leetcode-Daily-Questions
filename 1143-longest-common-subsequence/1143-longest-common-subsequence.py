class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        @lru_cache(None)
        def recc(m,n):
            if m == -1 or n == -1:
                return 0
            if s1[m] == s2[n]:
                return  recc(m-1,n-1)+1
            else:
                return max(recc(m-1,n),recc(m,n-1))
        return recc(m-1,n-1)
