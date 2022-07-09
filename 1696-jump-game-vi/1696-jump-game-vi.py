class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
            N = len(nums)
            heap = [] 
            for i in range(N-1, -1, -1):
                while heap and heap[0][1] > i + k:
                    heapq.heappop(heap)
                maxincluding = - nums[i] + (heap[0][0] if heap else 0)
                heapq.heappush(heap, (maxincluding, i))
                if i == 0: return -maxincluding