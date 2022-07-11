class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(cost):
                return 0
            x = []
            for j in range(1,3):
                x.append(dfs(i+j)+cost[i])
            return min(x)
            
        return min(dfs(0),dfs(1))
