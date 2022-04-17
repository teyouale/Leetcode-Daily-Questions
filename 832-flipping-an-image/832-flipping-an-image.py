class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            row = deque([])
            for j in i:
                val = 1-j
                row.appendleft(val)
            res.append(row)
        return res