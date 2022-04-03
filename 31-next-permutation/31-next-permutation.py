class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        currMax = n
        for i in range(n,0,-1):
            if nums[i-1] < nums[i]:break
            currMax-=1
        if not currMax:
            nums[:]=nums[::-1]
            return
        j = n
        while nums[j] <= nums[currMax-1]:
            j -= 1
        nums[currMax-1], nums[j] = nums[j], nums[currMax-1]
        nums[currMax:]= nums[len(nums)-1:currMax-1:-1]
