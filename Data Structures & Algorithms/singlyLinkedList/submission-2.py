class LinkedList:
    
    def __init__(self):
        self.arr = []
    def get(self, index: int) -> int:
        if 0 <= index < len(self.arr):
            return self.arr[index]
        else:
            return -1
    def insertHead(self, val: int) -> None:
        self.arr = [val] + self.arr
    def insertTail(self, val: int) -> None:
        self.arr = self.arr + [val]
    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.arr):
            del self.arr[index]
            return True
        else:
            return False
    def getValues(self) -> List[int]:
        return self.arr
