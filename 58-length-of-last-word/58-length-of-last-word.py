class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rsplit()
        return len(s[-1])