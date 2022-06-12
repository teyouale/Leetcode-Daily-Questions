class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen,max_,currentMax , l = {},0,0,0
        for i,v in enumerate(nums):
            if v in seen:
                while l < seen[v]+1:
                    currentMax-=nums[l]
                    l+=1
            seen[v]= i
            currentMax+=v
            max_ = max(currentMax,max_)
        return max_