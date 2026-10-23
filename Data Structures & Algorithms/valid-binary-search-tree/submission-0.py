# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left, right = - float('inf'), float('inf')
        return self.checkValid(left, root, right)
    def checkValid(self, left, node, right):
        if not node:
            return True
        elif left < node.val < right:
            return self.checkValid(left , node.left, node.val) and self.checkValid(node.val, node.right, right)
        else:
            return False