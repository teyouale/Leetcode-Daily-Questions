from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            A   A   B   A   B   B   A  K=1
                                i
                                    l
        """
        hashTable = defaultdict(int)
        l = 0
        res  = 0
        for i in range(len(s)):
            hashTable[s[i]]+=1
            while (i-l+1 )- max(hashTable.values()) > k:
                hashTable[s[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res
                               