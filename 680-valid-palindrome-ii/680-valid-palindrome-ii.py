class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s,i,j):
            while i<j:
                if s[i] != s[j]:return False
                i+=1
                j-=1
            return True
        l= 0
        r = len(s)-1
        while l< r:
            if s[l] != s[r]:
                return checkPalindrome(s,l,r-1) or checkPalindrome(s,l+1,r)
            l+=1
            r-=1
        return True