class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            h.append(-n)
        heapq.heapify(h)

        for i in range(k):
            res = - heapq.heappop(h)
        return res