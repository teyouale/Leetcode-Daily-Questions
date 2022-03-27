class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterTable = {}
        for k,v in enumerate(s):
            # if v in letterTable:
            letterTable[v]=k
        start = 0
        end =0
        res = []
        for k,v in enumerate(s):
            end = max(end,letterTable[v])
            if k == end:
                res.append(1+end-start)
                start = end+1
        return res