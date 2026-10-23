class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left ,right = 0, len(numbers) -1
        two_sum = numbers[left] + numbers[right]

        while two_sum != target:
            two_sum = numbers[left] + numbers[right]
            if two_sum < target:
                left += 1
            if two_sum > target:
                right -= 1
        return [left + 1, right + 1]