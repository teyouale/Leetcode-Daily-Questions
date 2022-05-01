class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sp = 0
        rp = 0
        ns = []
        nt = []
        
        for i in s:
            if i == '#'and ns:
                ns.pop()
                continue
            elif i == '#':
                continue
            ns.append(i)  
            
        for i in t:
            if i == '#'and nt:
                nt.pop()
                continue
            elif i == '#':
                continue
            nt.append(i)    
        
        return True if ns == nt else False