class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "/", "*"}:
                stack.append(int(token))
            else:
                digit1 = stack.pop()
                digit2 = stack.pop()
                match token:
                    case "+":
                        stack.append(digit2 + digit1)
                    case "-":
                        stack.append(digit2 - digit1)
                    case "*":
                        stack.append(digit2 * digit1)
                    case "/":
                        stack.append(int(digit2 / digit1))
            
        return int(stack[-1])