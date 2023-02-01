class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        combined = list(zip(ages,scores))
        combined.sort()
        n = len(ages) 
        @lru_cache(None)
        def dp(index):
            curr = combined[index][1]
            for next_ in range(index + 1, n):
                if combined[index][1] <= combined[next_][1] or combined[index][0] == combined[next_][0]:
                    curr = max(curr, dp(next_) + combined[index][1] )
            return curr
        res=  0
        for i in range(n):
            res = max(res,dp(i))
        return res