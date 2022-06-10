class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        l = 0
        r = 0
        res = set()
        ans = 0
        while r < len(s):
            curr = s[r]
            if curr not in  res:
                res.add(curr)
                ans = max(ans,len(res))
                r+=1
            else:
                res.remove(s[l])
                l+=1
            # print(res,ans,l,r,s[l:r])
        return ans                