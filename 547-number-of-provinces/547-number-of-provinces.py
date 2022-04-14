class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected[0])
        root =[i for i in range(n)]
        
#         Quick Union approch

        def find(y):
            x= y
            while x != root[x]:
                x = root[x]
            root[y] = x
            return x
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX
                
        for g,i in enumerate(isConnected):
            for k,j in enumerate(i):
                if g != k and j == 1:
                    union(g,k)
        return len(set([find(i) for i in range(n)]))