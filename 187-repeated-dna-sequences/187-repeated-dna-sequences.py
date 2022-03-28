from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
           "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
            l
                    i
        """
        if len(s) < 10:
            return []
        hashTable = defaultdict(int)
        visted = set()
        res = []
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr in visted:
                if curr not in res:
                    res.append(curr)
            visted.add(curr)                
        return res