class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        first = nums[0]
        if target == first:
            return 0
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            elif nums[l] <= nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
                
            
