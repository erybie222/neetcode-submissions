class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums) -1

        while left +1 < len(nums) and nums[left] > nums[left +1]:
            left += 1
        while right -1 > 0 and nums[right-1] < nums[right]:
            right -=1
        return min(nums[left],nums[right])