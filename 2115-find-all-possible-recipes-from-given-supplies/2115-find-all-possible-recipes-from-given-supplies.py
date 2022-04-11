from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # return []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        queue = supplies[:]
        for r,i in zip(recipes,ingredients):
            for j in i:
                graph[j].append(r)
                indegree[r]+=1
        while queue:
            current = queue.pop()
            if current in recipes:
                res.append(current)
            for neg in graph[current]:
                indegree[neg]-=1
                if indegree[neg] == 0:
                    queue.append(neg)
        return res