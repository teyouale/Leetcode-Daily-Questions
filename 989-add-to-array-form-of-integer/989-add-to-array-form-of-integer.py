class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a =  ''.join(map(str,num))
        return list(str(int(a)+k))