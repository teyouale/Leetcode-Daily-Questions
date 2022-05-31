class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()
        for i in range(k,len(s)+1):
            hashset.add(s[i-k:i])
        return len(hashset) == 2**k