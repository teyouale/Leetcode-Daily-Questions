class Solution:
    def maximum69Number (self, num: int) -> int:
        res = []
        change = False
        for i in str(num):
            if i == '9' or change:
                res.append(i)
            else:
                res.append('9')
                change = True
        return "".join(res)
