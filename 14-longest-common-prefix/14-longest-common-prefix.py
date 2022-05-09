class Solution:
    def getCommon(self,common,word):
        res = []
        min_ = min(len(common),len(word))
        for c,w in zip(common[:min_],word[:min_]):
            if c != w:
                break
            res.append(c)
        return ''.join(res)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for word in strs[1:]:
            res = self.getCommon(res,word)
        return res