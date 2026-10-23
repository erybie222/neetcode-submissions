class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        result = sorted(hashmap.items(), key = lambda x : x[1], reverse = True )
        result = result[:k]
        result = [n[0] for n in result]
        return result