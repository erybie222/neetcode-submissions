class MedianFinder:

    def __init__(self):
        self.small, self.large = [] , []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and ((-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
    def findMedian(self) -> float:
            if (len(self.small) + len(self.large)) == 0:
                return 0
            elif (len(self.small) + len(self.large))%2 == 0:
                val1, val2 = -1* self.small[0], self.large[0]
                median = (val1 + val2)/2
            else:
                if len(self.small) < len(self.large):
                    median = self.large[0]
                else:
                    median = -1 * self.small[0]
            return median