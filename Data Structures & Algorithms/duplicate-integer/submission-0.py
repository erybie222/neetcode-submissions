class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        used = set()
        for i in range(len(nums)):
            integer = nums[i]

            if integer not in used:
                used.add(integer)
            else:
                return True
        return False