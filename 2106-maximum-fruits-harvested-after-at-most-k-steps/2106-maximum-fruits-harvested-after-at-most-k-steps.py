class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        temp,_ = zip(*fruits) 
        fruit = {}
        for pos,num in fruits:
            fruit[pos] = num
            
        arr = [0]
        for i in range(fruits[-1][0]+1):
            arr.append(arr[-1]+fruit.get(i,0))
        left, right = sum(arr[:k+1]), sum(arr[k:])
        ans = 0
        sum_ = arr
        for pos in temp:
            r = min(max(2*pos+k-startPos,startPos),len(sum_)-2)
            l = max(min(2*pos-k-startPos,startPos),0)
            if abs(pos-startPos) <= k:
                if pos <= startPos: 
                    ans = max(ans,sum_[r+1]-sum_[pos])
                elif pos > startPos:
                    ans = max(ans,sum_[pos+1]-sum_[l])
        return ans