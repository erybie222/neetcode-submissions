class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)

        biggest = -self.smallHeap[0]
        smallest = self.bigHeap[0] if self.bigHeap else 0

        if biggest > smallest:
            heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, biggest)

        if len(self.smallHeap) + 1  < len(self.bigHeap):
            num = heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, -num)

        if len(self.bigHeap) + 1  < len(self.smallHeap):
            num = heapq.heappop(self.smallHeap)

            heapq.heappush(self.bigHeap, -num)
    def findMedian(self) -> float:
        twoHeapLength = len(self.smallHeap) + len(self.bigHeap)
        if twoHeapLength % 2 == 0:
            return (-self.smallHeap[0] + self.bigHeap[0])/2
        else:
            if len(self.smallHeap) > len(self.bigHeap):
                return -self.smallHeap[0]
            else:
                return self.bigHeap[0]