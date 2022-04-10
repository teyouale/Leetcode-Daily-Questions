from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        queue = [i for i in range(numCourses) if indegree[i]== 0 ]
        for i in queue:
            for j in graph[i]:
                indegree[j]-=1
                if indegree[j]==0:
                    queue.append(j)
        if len(queue) == numCourses:
            return queue 
        else:return []