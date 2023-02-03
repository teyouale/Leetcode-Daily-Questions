import bisect
class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = [0]
        for curr in w:
            self.prefixSum.append(self.prefixSum[-1]+curr)
        self.prefixSum.pop(0)
    def pickIndex(self) -> int:
        n = randint(1, self.prefixSum[-1])
        return bisect.bisect_left(self.prefixSum,n)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()