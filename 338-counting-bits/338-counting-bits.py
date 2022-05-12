class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i).replace('0b','').count('1'))
        return res