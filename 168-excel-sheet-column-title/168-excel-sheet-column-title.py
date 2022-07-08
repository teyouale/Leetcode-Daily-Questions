class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        curr = columnNumber
        while curr > 0:
            x , n = divmod(curr-1,26)
            curr = x
            res.append(chr(65+n))
            # res = ''.join((chr(65+n), res))
        return ''.join(res[::-1])