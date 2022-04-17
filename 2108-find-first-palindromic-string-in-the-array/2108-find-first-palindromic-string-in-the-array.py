class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrom(string):
            l = 0
            r = len(string)-1
            while l <r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True
            
        for i in words:
            if isPalindrom(i):
                return i
        return ''