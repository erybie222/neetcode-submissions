class MedianFinder:
    def __init__(self):
        self.numlist = []
    def addNum(self, num: int) -> None:
        isAdded = False
        for id in range(len(self.numlist)):
            curr_num = self.numlist[id]
            if curr_num > num:
                self.numlist.insert(id, num)
                isAdded = True
                break
        if not isAdded:
            self.numlist.append(num)
    def findMedian(self) -> float:
        length = len(self.numlist)
        if length == 0:
            return 0
        elif length % 2 == 0:
            mid_id1, mid_id2 = length/2 - 1 , length/2
            median = (self.numlist[int(mid_id1)] + self.numlist[int(mid_id2)])/2
        else:
            mid_id = (length//2)
            median = self.numlist[int(mid_id)]
        return median