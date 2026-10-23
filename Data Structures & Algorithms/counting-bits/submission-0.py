class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n +1):
            num = i
            curr = 0
            while num > 0:
                curr += num%2
                num = num >> 1
            output.append(curr)
        return output