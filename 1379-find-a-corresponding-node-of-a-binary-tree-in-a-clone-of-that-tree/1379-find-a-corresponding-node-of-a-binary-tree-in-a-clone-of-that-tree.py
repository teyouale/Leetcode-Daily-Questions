# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, o: TreeNode, c: TreeNode, target: TreeNode) -> TreeNode:
        clone = [o]
        orginal =[c]
        while clone:
            for i in range(len(clone)):
                currc = clone.pop(0)
                curro = orginal.pop(0)

                if currc == target:
                    return curro
                if currc.left:clone.append(currc.left)
                if currc.right:clone.append(currc.right) 
                if curro.left:orginal.append(curro.left)
                if curro.right:orginal.append(curro.right) 
                    