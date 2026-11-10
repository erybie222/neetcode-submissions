class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            distance = x**2 + y**2
            h.append([distance, [x, y]])
        heapq.heapify(h)
        res = []
        for i in range(k):
            dist, point = heapq.heappop(h)
            res.append(point)
        return res