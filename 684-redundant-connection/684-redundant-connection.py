class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # return [1,2]
        root = [i for i in range(len(edges))]
        
        def find(x):
            if x == root[x]:
                return x
            root[x]=find(root[x])
            return root[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            elif rootX != rootY :
                root[rootY] = rootX
                return True
        for x,y in edges:
            if not union(x-1,y-1):
                return [x,y]
