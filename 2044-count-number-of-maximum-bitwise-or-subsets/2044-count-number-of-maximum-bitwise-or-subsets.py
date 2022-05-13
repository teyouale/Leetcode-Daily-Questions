class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        def dfs(temp,idx):
            res.append(temp[:])
            for i in range(idx,len(nums)):
                temp.append(nums[i])
                dfs(temp,i+1)
                temp.pop()
        dfs([],0)
        y = Counter([])
        for i in res[1:]:
            x = i[0]
            for j in i[1:]:
                x|=j
            y[x]+=1
        return y.most_common(1)[0][1]            