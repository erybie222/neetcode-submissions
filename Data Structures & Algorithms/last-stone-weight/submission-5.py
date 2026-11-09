class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        h = [-s for s in stones]
        heapq.heapify(h)
        

        while len(h) >= 2:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x > y:
                heapq.heappush(h, -(x - y))
            
        if h:
            res = -heapq.heappop(h)

        return res
        

        