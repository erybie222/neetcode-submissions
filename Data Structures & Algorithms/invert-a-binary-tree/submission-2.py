# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, node):
        if not node or (not node.left and not node.right):
            return node
        else:
            node.left , node.right = node.right, node.left
            self.invert(node.left)
            self.invert(node.right)
        



    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        
            
        self.invert(curr)
        return curr