from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a,b in prerequisites:
            graph[b].append(a)
            
        visted , cycle = set(),set()
        def dfs(course):
            if course in cycle:return False
            if course in visted:return True
            
            cycle.add(course)
            for i in graph[course]:
                if not dfs(i):return False
            cycle.remove(course)
            visted.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True