class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre  = [0]
        suf = [0]
        for i in nums:
            pre.append(pre[-1]+i)
        for i in nums[::-1]:
            suf.append(suf[-1]+i)
        pre.pop(0)
        suf.pop(0)
        suf[:] = suf[::-1]
        for i in range(len(nums)):
            if pre[i] == suf[i]:
                return i
        return -1