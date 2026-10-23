# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            lDepth = depth(node.left)
            if lDepth == -1:
                return -1
            rDepth = depth(node.right)
            if rDepth == -1 or abs(rDepth - lDepth) > 1:
                return -1
            if abs(lDepth - rDepth) > 1:
                isBalanced = False
            return 1 + max(lDepth, rDepth)
        
        return depth(root) != -1