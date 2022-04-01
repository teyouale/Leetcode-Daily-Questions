class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l = 0
        # r = len(s) - 1
        # while (l<=r):
        #     s[l] , s[r] = s[r] , s[l]
        #     l+=1
        #     r-=1
            
        for i in range(len(s)//2):s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i] 