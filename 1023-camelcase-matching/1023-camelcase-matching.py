class Solution:
    def isCamelCase(self,word,pattern):
        wp = 0
        pp = 0
        
        # if len(pattern) > len(word):
            # return False
        count = 0
        while pp < len(pattern) and wp < len(word):
            # print(wp,pp)
            if word[wp] == pattern[pp]:
                wp+=1
                pp+=1
                count+=1
            elif word[wp].islower()  and pattern[pp].islower():
                if  word[wp]==pattern[pp]:
                    wp+=1
                    pp+=1
                    count+=1
                    
                else:
                    wp+=1
            # elif word[wp].
            elif word[wp].islower()  and pattern[pp].isupper():
                if  word[wp]==pattern[pp]:
                    wp+=1
                    pp+=1
                    count+=1
                    
                else:
                    wp+=1
            else:
                return False
        
        if count != len(pattern):
            return False
        while wp < len(word):
            if word[wp].isupper():
                return False
            wp+=1
        return True
        
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for q in queries:
            res.append(self.isCamelCase(q,pattern))
        return res