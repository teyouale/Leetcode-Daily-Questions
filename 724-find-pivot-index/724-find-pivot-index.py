class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre  = 0
        sum_ = 0
        for i in nums:sum_+=i
        for i in range(len(nums)):
            if pre == sum_-pre-nums[i]:
                return i
            pre+=nums[i]
        return -1