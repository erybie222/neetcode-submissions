
class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (liczby zanegowane), mniejsza połowa
        self.large = []  # min-heap, większa połowa

    def addNum(self, num: int) -> None:
        # 1. wrzuć do small
        heapq.heappush(self.small, -num)
        # 2. największy z small przenieś do large, żeby każdy element small był <= każdego z large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # 3. wyrównaj rozmiary: small może mieć co najwyżej 1 więcej
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2