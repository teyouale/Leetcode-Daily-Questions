class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visted = set()
        def dfs(i,curr):
            if (i,not curr) in visted:
                return False
            if (i,curr) in visted:
                return True
            visted.add((i,curr))
            for j in graph[i]:
                if not dfs(j,not curr):
                    return False
            return True
        n = len(graph)
        for i in range(n):
            if (i,True) not in visted and (i,False) not in visted:
                if not dfs(i,True):
                    return False
        return True