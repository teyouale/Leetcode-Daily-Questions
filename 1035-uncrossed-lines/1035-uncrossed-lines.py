class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        @lru_cache(None)
        def recc(m,n):
            if m == -1 or n == -1:
                return 0
            if nums1[m] == nums2[n]:
                return 1 + recc(m-1,n-1)
            else:
                return max(recc(m-1,n),recc(m,n-1))
        return recc(m-1,n-1)