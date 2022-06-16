class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxL = 0
        
        def findPaildrom(l,r):
            nonlocal maxL,res
            
            while l >=0 and r < len(s) and s[l]==s[r]:
                if (r-l+1) > maxL:
                    res = s[l:r+1]
                    maxL = r-l+1
                l-=1
                r+=1
        for i in range(len(s)):
            findPaildrom(i,i)
            findPaildrom(i,i+1)
        return res            
            
            
            