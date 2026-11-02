class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opened, closed, current):
            if  closed == 0:
                res.append("".join(current))
                return
            if opened > 0:
                current.append('(')
                dfs(opened - 1, closed , current)
                current.pop()
            if closed > opened:
                current.append(')')
                dfs(opened, closed - 1 , current)
                current.pop()
            

        dfs(n, n , [])
        return res