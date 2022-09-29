class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0]*n
        ans = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        queue = deque([k for k in range(n) if indegree[k]==0])
        
        while queue:
            curr = queue.popleft()
            for neg in graph[curr]:
                indegree[neg]-=1
                t =  list(set(ans[curr] + [curr] + ans[neg])) 
                t.sort()
                ans[neg]=t
                if indegree[neg] == 0:
                    queue.append(neg)
        return list(ans)