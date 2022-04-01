class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre  = [0]
        for i in nums:
            pre.append(pre[-1]+i)
        pre.pop(0)
        for i in range(len(nums)):
            if pre[i] == pre[-1]-pre[i]+nums[i]:
                return i
        return -1