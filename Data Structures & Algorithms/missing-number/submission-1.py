class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = {i: False for i in range(len(nums)+1)}
        for num in nums:
            numbers[num] = True

        for key, value in numbers.items():
            if value == False:
                return key
