class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(firstList) and p2 < len(secondList):
            currF = firstList[p1]
            currS = secondList[p2]
            if currF[0] <= currS[0] <= currF[1] or currS[0] <= currF[0] <= currS[1]:
                lb = max(currF[0],currS[0])
                rb = min(currF[1],currS[1])
                res.append([lb,rb])
            # elif :
                # lb = max(currF[0],currS[0])
                # rb = min(currF[1],currS[1])
                # res.append([lb,rb])
                
            if currF[1] < currS[1]:
                    p1+=1
            elif currF[1] > currS[1]:
                    p2+=1
            else:
                    p1+=1
                    p2+=1
        return res
