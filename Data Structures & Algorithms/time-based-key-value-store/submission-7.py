class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        l, r = 0, len(self.storage[key]) - 1
        pivot = 0
        while l <= r:
            pivot = (l + r )// 2
            if self.storage[key][pivot][1] < timestamp:
                l = pivot + 1
            elif self.storage[key][pivot][1] > timestamp:
                r = pivot - 1
            else:
                return self.storage[key][pivot][0]
        if r >= 0:
            return self.storage[key][r][0]
        else:
            return ""