from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        res = []
        visted , cycle = set(),set()
        def dfs(course):
            if course in cycle: return False
            if course in visted:return True
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre):return False
            cycle.remove(course)
            visted.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):return []
        return res[::-1]
        