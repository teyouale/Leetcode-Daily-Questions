class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in ops:
            if i == 'D':
                res.append(str(int(res[-1])*2))
            elif i == 'C':
                res.pop()
            elif i == '+':
                res.append(str(int(res[-1])+int(res[-2])))
            else:
                res.append(i)
        return sum(map(int,res))