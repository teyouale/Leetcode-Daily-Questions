class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_ = float("inf")
        for i in range(n):
            count = 0 
            operations = 0
            for j in range(i, n):
                if blocks[j] == "W":
                    operations += 1
                count += 1
                if count == k:
                    min_ = min(min_, operations)
        return min_