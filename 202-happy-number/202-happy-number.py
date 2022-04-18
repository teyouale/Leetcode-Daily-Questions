class Solution:
    def isHappy(self, num: int) -> bool:
        visted = set()
        while num not in visted:
            if num ==1:return True
            visted.add(num)
            num= sum([ int(i)**2 for i in str(num)])
        return False