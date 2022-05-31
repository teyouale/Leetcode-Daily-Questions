class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = set()
        i =0
        n = len(s)
        while i+k <= n :
            res.add(s[i:i+k])
            i+=1
        w =2**k
        return len(res) == w

      