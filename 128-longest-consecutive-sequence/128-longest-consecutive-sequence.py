from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root={}
        ans = defaultdict(int)
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootX]= rootY
                
        for i in nums:
            if not i in root:
                root[i]=i
            if i-1 in root:
                union(i,i-1)
            if i+1 in root :
                union(i,i+1)
                
        for i in root.keys():
            ans[find(i)]+=1
        return max(ans.values())
