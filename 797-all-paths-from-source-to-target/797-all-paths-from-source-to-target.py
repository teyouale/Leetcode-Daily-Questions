class Solution:
    def allPathsSourceTarget(self, Ggraph: List[List[int]]) -> List[List[int]]:
        n = len(Ggraph)
        if not Ggraph:
            return []
        graph = defaultdict(list)
        indegree = [0] * n
        for u,k in enumerate(Ggraph):
            for v in k:
                graph[u].append(v)
                indegree[v] += 1
        queue = deque([(0, [0])])
        res = []
        ans = []
        visted = set()
        while queue:
            curr, path = queue.popleft()
            for ne in graph[curr]:
                if ne == n-1:
                    ans.append(path+[ne])
                if ne not in visted:
                    visted.add(ne)
                    queue.append((ne, path+[ne]))
                    visted.remove(ne)
        # print(ans)
        return ans