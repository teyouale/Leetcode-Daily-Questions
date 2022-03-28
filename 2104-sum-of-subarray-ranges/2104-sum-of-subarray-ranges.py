class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            min_,max_ = nums[i],nums[i]
            for j in range(i,len(nums)):
                min_ = min(min_,nums[j])
                max_ = max(max_,nums[j])
                
                count+=(max_-min_)
        return count
                