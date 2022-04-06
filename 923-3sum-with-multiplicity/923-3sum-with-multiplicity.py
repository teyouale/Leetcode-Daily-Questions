from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9 + 7
        arr.sort()
        cnt = Counter(arr) 
        res, i, l = 0, 0, len(arr)
        while i < l:
            j, k = i, l-1 
            while j < k:
                if arr[i]+arr[j]+arr[k] < target:
                    j += cnt[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= cnt[arr[k]]
                else:  
                    if arr[i] != arr[j] != arr[k]:  
                        res += cnt[arr[i]]*cnt[arr[j]]*cnt[arr[k]]
                    elif arr[i] == arr[j] != arr[k]: 
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*cnt[arr[k]]//2 
                    elif arr[i] != arr[j] == arr[k]:  
                        res += cnt[arr[i]]*cnt[arr[j]]*(cnt[arr[j]]-1)//2  
                    else:
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*(cnt[arr[i]]-2)//6
                    j += cnt[arr[j]]
                    k -= cnt[arr[k]]
            i += cnt[arr[i]] 
        return res%mod