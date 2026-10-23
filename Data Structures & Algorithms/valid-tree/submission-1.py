class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        adj = { i: set() for i in range(n)}
        visited = set()
        
        for node1, node2 in edges:
            adj[node1].add(node2)
            adj[node2].add(node1)

        def dfs(node , prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0,-1):
            return False
        if len(visited) == n:
            return True
        return False
