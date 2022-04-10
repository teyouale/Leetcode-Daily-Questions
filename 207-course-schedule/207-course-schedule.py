from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        queue = [i for i in range(len(indegree)) if indegree[i]==0]
        # count=0
        # while  queue:
        for j in queue:
            for i in graph[j]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)
        return len(queue)==numCourses
