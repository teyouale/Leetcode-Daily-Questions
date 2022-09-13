class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted = set()
        def dfs(i):
            if i in visted:
                return
            visted.add(i)
            for n in rooms[i]:
                dfs(n)
        n = len(rooms)
        count = 0
        for i in range(n):
            if i not in visted:
                dfs(i)
                count+=1
        return count == 1