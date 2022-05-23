class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(index,x,y):
                if x < 0 or y < 0:
                    return float('-inf')
                if index == len(strs):
                    return 0
                o ,z = strs[index].count('1') , strs[index].count('0')
                temp1 = 1+dfs(index+1,x-z,y-o)
                temp2 = dfs(index+1,x,y)
                return max(temp1,temp2)
        return dfs(0,m,n)
    
     
   
    