class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target > 0:
            if target&1:
                target -=1
            else:
                maxDoubles-=1
                target>>=1
            count+=1
        return count + target-1
                