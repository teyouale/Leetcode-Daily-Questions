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
        ans = []
        while queue:
            curr, path = queue.popleft()
            if curr == n-1:
                ans.append(path)
            for ne in graph[curr]:
                queue.append((ne, path+[ne]))
        # print(ans)
        return ans