# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, depth):
        if not node:
            return depth
        else:
            l_depth = self.dfs(node.left, depth + 1)
            r_depth = self.dfs(node.right, depth + 1)
            return max(l_depth, r_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.dfs(root, 0)
        return depth
        