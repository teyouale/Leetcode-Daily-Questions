class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a , b = 0,0
        res =[]
        while a < len(nums1)  and b < len(nums2):
            if nums1[a] < nums2[b]:
                if a < m: 
                    res.append(nums1[a])
                a+=1
            else:
                res.append(nums2[b])
                b+=1
        
        while  a < len(nums1) and a < m:
            res.append(nums1[a])
            a+=1
        while  b < len(nums2):
            res.append(nums2[b])
            b+=1
        for i in range(len(res)):
            nums1[i] = res[i]
