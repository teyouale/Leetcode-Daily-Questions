# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        stack = [root]
        while stack:
            temp = float('-inf')
            for _ in range(len(stack)):
                curr = stack.pop(0)
                temp=max(temp,curr.val)
                if curr.left:stack.append(curr.left)
                if curr.right:stack.append(curr.right)
            res.append(temp)
        return res