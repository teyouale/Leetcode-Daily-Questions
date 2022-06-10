class Solution:
    def countOdds(self, l: int, h: int) -> int:
        return (h+1-l)//2 + (h%2 & l%2)