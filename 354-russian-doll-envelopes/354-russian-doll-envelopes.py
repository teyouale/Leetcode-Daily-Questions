class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
            es = [ e[1] for e in sorted( envelopes, key=lambda x: (x[0], -x[1]))]
            res = []
            for e in es:
                pos = bisect_left( res, e )
                if pos >= len(res):
                    res.append( e )
                else:
                    res[pos] = e
            return len(res)