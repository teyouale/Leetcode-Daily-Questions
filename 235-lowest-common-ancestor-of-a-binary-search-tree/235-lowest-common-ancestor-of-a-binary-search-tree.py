# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentValue = root.val
        if p.val > currentValue and q.val > currentValue:
            return self.lowestCommonAncestor( root.right, p, q)
        elif p.val < currentValue and q.val < currentValue:
            return self.lowestCommonAncestor( root.left, p, q)
        else:
            return root
