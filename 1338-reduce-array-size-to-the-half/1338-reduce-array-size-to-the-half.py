from collections import Counter
from heapq import *
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        item = []
        for k,v in counter.items():
            heappush(item,-v)
        current = 0
        count = 0
        while current < len(arr)//2:
            x = -heappop(item)
            count+=1
            current+=x
        return count
        
        
        