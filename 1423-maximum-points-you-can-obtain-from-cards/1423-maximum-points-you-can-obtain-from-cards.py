class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        psum = [0]
        totalSum =0
        res= 0
        l = 1
        n = len(cardPoints)
        d = n-k
        r = d
        
        
        for i in cardPoints:
            totalSum+=i
            psum.append(psum[-1]+i)
        
        while r <= n:
            curr = psum[r]-psum[l-1]
            res= max(res,totalSum-curr)
            l+=1
            r+=1
        return res
            
            