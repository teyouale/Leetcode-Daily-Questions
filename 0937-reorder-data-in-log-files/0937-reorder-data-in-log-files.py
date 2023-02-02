class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = {}
        digit = []
        
        for log in logs:
            splited = log.split(' ')
            if splited[1][0].isalpha():
                letter[log] = ' '.join(splited[1:])
            else:
                digit.append(log)
                
        l = sorted(letter.items(),key = lambda x:(x[1],x[0]))
        
        res=  []
        for k,v in l:
            res.append(k)
        res.extend(digit)
        return res