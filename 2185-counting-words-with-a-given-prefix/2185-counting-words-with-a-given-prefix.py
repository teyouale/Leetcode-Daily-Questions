class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            for i in range(len(word)):
                if pref == word[:i+1]:
                    res+=1
                    break
        return res