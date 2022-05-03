class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums == nums:
              return 0
        start = 0
        while sorted_nums[start] == nums[start]:
               start += 1
        end = len(nums) - 1
        while sorted_nums[end] == nums[end]:
               end -= 1

        return end + 1 - start