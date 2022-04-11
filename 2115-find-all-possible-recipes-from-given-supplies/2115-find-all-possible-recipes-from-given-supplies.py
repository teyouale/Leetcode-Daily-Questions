from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # return []
        graph = defaultdict(list)
        indegree = [0]*len(recipes)
        res = []
        queue = supplies[:]
        for k,(r,i) in enumerate((zip(recipes,ingredients))):
            for j in i:
                graph[j].append(r)
                indegree[k]+=1
        while queue:
            current = queue.pop()
            if current in recipes:
                res.append(current)
            for neg in graph[current]:
                indegree[recipes.index(neg)]-=1
                if indegree[recipes.index(neg)] == 0:
                    queue.append(neg)
        return res