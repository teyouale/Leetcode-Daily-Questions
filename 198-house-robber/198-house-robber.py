class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0]
        idx = 0
        for i in nums:
            t = max(i+dp[-2],dp[-1])
            dp.append(t)
        print(dp)
        return max(dp[-2],dp[-1])