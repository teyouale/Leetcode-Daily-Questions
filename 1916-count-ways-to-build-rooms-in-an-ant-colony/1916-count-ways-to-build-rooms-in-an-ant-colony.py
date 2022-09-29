import sys
sys.setrecursionlimit(10**6)
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        graph = defaultdict(list)
        n = len(prevRoom)
        MOD = 10**9 + 7
        for i in range(1,n):
            u, v = i,prevRoom[i]
            graph[v].append(u)
        def dfs(i):
            if i in visted:
                return 0
            visted.add(i)
            ans = 1
            for ne in graph[i]:
                ans += dfs(ne)
            dp[i] = ans
            return ans

        visted = set()
        dp = [0]*n
        dfs(0)
        x = dp[0]
        for i in dp[1:]:
            x *= i
        return  (factorial(n)//x)%MOD
