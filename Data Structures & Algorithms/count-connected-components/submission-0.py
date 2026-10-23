class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0

        adj = {i: [] for i in range(n)}

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        connected = 0
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            if node == parent:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei, node)
            return 
        
        for i in range(n):
            if i not in visited:
                connected+=1
                dfs(i, -1)
        return connected
