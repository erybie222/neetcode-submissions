class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        h = []
        heapq.heapify(h)
        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h) >= 2:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x > y:
                heapq.heappush(h, -(x - y))
            
        if h:
            res = -heapq.heappop(h)

        return res
        

        