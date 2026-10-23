# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = 0

    def dfs(self, node, maxNode):
            if not node:
                return
            else:
                if node.val >= maxNode:
                    self.counter += 1
                    maxNode = node.val
                self.dfs(node.left, maxNode)
                self.dfs(node.right, maxNode)

    

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)

        return self.counter