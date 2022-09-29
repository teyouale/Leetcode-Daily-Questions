class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0]*n
        ans = [set() for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        queue = deque([k for k in range(n) if indegree[k]==0])
        
        while queue:
            curr = queue.popleft()
            for neg in graph[curr]:
                indegree[neg]-=1
                ans[neg].add(curr)
                ans[neg].update(ans[curr])
                if indegree[neg] == 0:
                    queue.append(neg)
        return [sorted(i) for i in ans]