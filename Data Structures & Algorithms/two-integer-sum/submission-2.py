class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for index, n in enumerate(nums):
            hash_map[n] = index

        for index, n in enumerate(nums):
            goal = target - n
            if goal in hash_map and hash_map[goal] != index:
                return [index, hash_map[goal]]            