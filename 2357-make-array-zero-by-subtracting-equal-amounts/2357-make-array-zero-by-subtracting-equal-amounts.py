class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set(nums)
        if 0 in unique:
            return len(unique)-1
        return len(unique)