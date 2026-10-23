class Solution:
    def reverseBits(self, n: int) -> int:
        new = 0
        for i in range(32):
            last = n & 1
            n = n >> 1
            new = new << 1
            if last == 1:
                new += 1
        return new
