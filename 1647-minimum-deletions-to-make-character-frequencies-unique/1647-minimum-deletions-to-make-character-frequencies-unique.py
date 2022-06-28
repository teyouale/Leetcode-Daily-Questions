class Solution:
    def minDeletions(self, s: str) -> int:
        c = list(Counter(s).values())
        res =0 
        vist = set()
        for k,v in enumerate(c):
            t =v
            if t in vist:
                while t in vist and t > 0:
                    t-=1
                    res+=1
                # c[k]=t
            # else:
            vist.add(t)
        return res