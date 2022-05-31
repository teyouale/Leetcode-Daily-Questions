class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res , n , w ,i= set(),len(s),1<<k,0
        while i+k <= n :
            res.add(s[i:i+k])
            i+=1
        return len(res) == w

      