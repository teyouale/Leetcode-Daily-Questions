# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        res = [root]
        ans = 0
        while res:
            ans =0
            for _ in range(len(res)):
                curr = res.pop(0)
                if curr.left:res.append(curr.left)
                if curr.right:res.append(curr.right)
                ans+=curr.val

        return ans