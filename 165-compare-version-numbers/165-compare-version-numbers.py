class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        val1 = [int(i)  for  i in version1.split('.')]
        val2 = [int(i) for i in version2.split('.') ]       
        for x in range(max(len(val1),len(val2))):
            v1 = val1[x] if x < len(val1) else 0 
            v2 = val2[x] if x < len(val2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0