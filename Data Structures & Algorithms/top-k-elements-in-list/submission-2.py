class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times_used = {}
        for num in nums:
            if num in times_used:
                times_used[num] += 1
            else:
                times_used[num] = 1
        sorted_items = sorted(times_used.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
