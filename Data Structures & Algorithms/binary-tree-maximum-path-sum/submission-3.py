# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = float('-inf')
    def maxPath(self, node):
        if not node:
            return 0
        else:
            leftVal = max(0, self.maxPath(node.left))
            rightVal =  max(0, self.maxPath(node.right))
            self.res = max(self.res, node.val + leftVal + rightVal)
            return node.val + max(leftVal, rightVal)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath(root)
        return self.res
        