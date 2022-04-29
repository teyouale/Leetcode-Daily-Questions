class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(start):
            if self.loop: return    

            for neib in graph[start]:
                if dist[neib] >= 0 and dist[neib] == dist[start]:
                    self.loop = True
                elif dist[neib] < 0:
                    dist[neib] = dist[start]^1
                    dfs(neib)
            
        n = len(graph) 
        self.loop, dist = False, [-1] *(n)
        
        for i in range(n):
            if self.loop: return False    
            if dist[i] == -1:
                dist[i] = 0
                dfs(i)
                
        return True