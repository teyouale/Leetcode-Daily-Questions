class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        index = 0
        # current = 1
        while (index < len(heights)-1):
            if heights[index] < heights[index+1]:
                # heapq.
                if ladders:
                    heapq.heappush(heap,abs(heights[index]-heights[index+1]))
                    ladders-=1
                else:
                    brick = heapq.heappushpop(heap,abs(heights[index]-heights[index+1]))
                    if bricks-brick >= 0:bricks-=brick
                    else:break

            # print(heap,bricks,ladders,heights[index])
            index+=1
        return index