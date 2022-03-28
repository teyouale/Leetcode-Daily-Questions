class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        oc 4
        c 2
        o c 
        
        """
        if len(s)%2 ==1:
            return False
        oc = o = c =0
        n = len(s)
        for i in range(n):
            if locked[i] == '0': oc+=1
            else:
                if s[i] == ")":
                    c+=1
                else:o+=1
            if  oc+o-c < 0:return False
        
        oc = o = c =0
        for i in range(n-1,-1,-1):
            if locked[i] == '0': oc+=1
            else:
                if s[i] == "(":  o+=1
                else:c+=1
            if  oc-o+c < 0:return False
        return True