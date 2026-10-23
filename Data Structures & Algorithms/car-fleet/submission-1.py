class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for p, s in sorted(zip(position, speed), key = lambda x : x[0], reverse = True):
            stack.append((target - p)/s)
            if  len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)

        
