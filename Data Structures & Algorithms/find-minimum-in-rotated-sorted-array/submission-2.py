class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) -1
        minVal = float('inf')
        while l <= r:
            pivot = (l + r )// 2
            minVal = min(minVal, nums[pivot])
            if nums[pivot] < nums[r]:
                r = pivot - 1
            else:
                
                l = pivot + 1
        
        return minVal
