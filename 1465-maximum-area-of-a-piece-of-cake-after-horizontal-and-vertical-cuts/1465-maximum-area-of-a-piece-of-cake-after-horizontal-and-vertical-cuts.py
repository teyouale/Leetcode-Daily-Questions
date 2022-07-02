class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9 + 7
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        mh = mv = 0
        for i in range(1,len(horizontalCuts)):
            mh = max(mh,horizontalCuts[i]-horizontalCuts[i-1])   
        for i in range(1,len(verticalCuts)):
            mv = max(mv,verticalCuts[i]-verticalCuts[i-1])   
        res = mh*mv    
        return res % mod
                
        
        