class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        cNum = 0
        cCount, mCount = 0,0
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                cNum = num

                while cNum in nums:
                    cCount += 1
                    mCount = max(mCount, cCount) 
                    cNum += 1
                cCount = 0
        return mCount            