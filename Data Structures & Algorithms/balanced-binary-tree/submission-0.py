# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def depth(node):
            nonlocal isBalanced
            if not node:
                return 0
            lDepth, rDepth = depth(node.left), depth(node.right)
            if abs(lDepth - rDepth) > 1:
                isBalanced = False
            return 1 + max(lDepth, rDepth)
        depth(root)
        return isBalanced