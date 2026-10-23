class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)  
            elif stack and stack[-1] == pairs[bracket]:
                stack.pop()
            else:
                return False

        return not stack