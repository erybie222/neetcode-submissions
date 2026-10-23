# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = collections.deque()
        binaryTree = []

        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    binaryTree.append("null")
                    continue
                else:
                    binaryTree.append(str(node.val))
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
        return " ".join(binaryTree)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        else:
            data = list(data.split(" "))
            queue = collections.deque()
            root = TreeNode(int(data[0]))
            queue.append(root)
            i = 1
            while queue:
                parent = queue.popleft()
                node1 = data[i]
                if node1 != "null":
                    node1 = TreeNode(int(node1))
                    parent.left = node1
                    queue.append(node1)

                node2 = data[i+1]
                if node2 != "null":
                    node2 = TreeNode(int(node2))
                    parent.right = node2
                    queue.append(node2)
                i += 2
            return root
                


            


                    

