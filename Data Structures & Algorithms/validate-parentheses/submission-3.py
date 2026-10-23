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
            else:
                if stack and stack[-1] == pairs[bracket]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False