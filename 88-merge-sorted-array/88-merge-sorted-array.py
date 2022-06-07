class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a , b , c = m-1,n-1 , len(nums1)-1
        
        while a > -1 and b > -1:
            if nums1[a] > nums2[b]:
                nums1[c] = nums1[a]
                # nums1[a] = 0
                c-=1
                a-=1
            else:
                nums1[c] = nums2[b]
                b-=1
                c-=1
        while b > -1:
            nums1[c] = nums2[b]
            b-=1
            c-=1
                