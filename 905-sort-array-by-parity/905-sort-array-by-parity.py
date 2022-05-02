class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l =0 
        r = len(nums)-1
        # for i in nums:
        while l<r:
            while nums[r] % 2 == 1 and l<r:
                r-=1
            if nums[l] % 2 == 1 and nums[r]%2 == 0:
                nums[l] , nums[r] = nums[r],nums[l]
            l+=1
        return nums    
            