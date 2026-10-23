# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.dfs_recursive(root)
        return self.nodes[k-1]
    def dfs_recursive(self, node):
        if not node:
            return
        self.dfs_recursive(node.left)
        self.nodes.append(node.val)
        self.dfs_recursive(node.right)