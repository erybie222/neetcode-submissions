# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def dfs(node):
            if not node:
                return 0
            else:
                lDepth, rDepth = dfs(node.left) , dfs(node.right)
                self.maxD = max(self.maxD, lDepth + rDepth)
                return 1 + max(lDepth, rDepth)

        dfs(root)
        return self.maxD