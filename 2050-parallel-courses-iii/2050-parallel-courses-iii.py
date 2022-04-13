from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], t: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0]*(n+1)
        for a,b in relations:
            indegree[b]+=1
            graph[a].append(b)
        heap = []
        for i in range(1, n + 1):
            if indegree[i] == 0:
                heappush(heap, (t[i-1], i))
        globaltime = 0
        while heap:
            currtime,curridx = heapq.heappop(heap)
            globaltime=currtime
            for neg in graph[curridx]:
                indegree[neg]-=1
                if indegree[neg]==0:
                           heapq.heappush(heap,(globaltime+t[neg-1],neg))
        return globaltime
  