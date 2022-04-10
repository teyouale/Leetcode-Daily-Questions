class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNode = {}
        visted , cycle = set(),set()
        res = []
        def dfs(node):
            if node in safeNode:
                return safeNode[node]
            safeNode[node] = False
            for j in graph[node]:
                if not dfs(j):
                    return False
            safeNode[node] = True
            return safeNode[node]
        for i in range(len(graph)):
            if dfs(i):res.append(i)
        
        return res