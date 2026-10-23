class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i, n in enumerate(nums):
            diff = 0 - n

            l, r = i +1 , len(nums) -1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum < diff:
                    l += 1
                elif two_sum == diff:
                    result.add((nums[i] ,nums[l], nums[r] ))
                    l += 1
                    r -= 1
                else:
                    r-= 1  
        return list(result)