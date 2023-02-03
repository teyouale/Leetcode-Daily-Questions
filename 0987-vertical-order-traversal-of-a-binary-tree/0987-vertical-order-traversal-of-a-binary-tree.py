# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashTable = defaultdict(list)
        def dfs(node,x,y):
            if not node:
                return 
            hashTable[x].append([node.val,x,y])
            # print(x,y,nove.val)            
            dfs(node.left,x-1,y+1)
            dfs(node.right,x+1,y+1) 
            
        res=[]
        dfs(root,0,0)
        for key,items in sorted(hashTable.items()):
            curr = []
            for val,x,y in sorted(items,key=lambda x:(x[2],x[1],x[0])):
                curr.append(val)
            res.append(curr)
        return res