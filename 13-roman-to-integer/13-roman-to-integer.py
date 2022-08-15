class Solution:
    def romanToInt(self, s: str) -> int:
        hashTable = {
            "I":1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        res = 0
        pre = 0
        rule = {
            'I':('V','X'),
            'X':('L','C'),
            'C':('D','M'),
        }
        for i in s:
            currentRule = rule.get(pre,None)
            if currentRule:
                x , y = currentRule
                rescurr = hashTable[i]  
                if i == x:
                    rescurr = hashTable[x] - hashTable[pre]
                    res-=hashTable[pre]
                elif i == y:
                    rescurr = hashTable[y] - hashTable[pre]
                    res-=hashTable[pre]
                res+=rescurr
            else:
                res+=hashTable[i]
            pre = i
        return res