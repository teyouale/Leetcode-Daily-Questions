class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ''
        
        res = []
        dct = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        temp = dct[digits[0]]
        if len(digits) == 1:
            return temp
        
        for i in digits[1:]:
            x = []
            for k in temp:
                for j in dct[i]:
                    x.append(k+j)
                    # res.append(k+j)
            res = x[:]
            temp = x[:]
        return res