"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        hash_map = {}
        hash_map[node] = Node(node.val)

        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor not in hash_map:
                    hash_map[neighbor] = Node(neighbor.val)
                    dfs(neighbor)
                hash_map[node].neighbors.append(hash_map[neighbor])
        dfs(node)
        return hash_map[node]

            