class Solution:
    def numberToWords(self, num: int) -> str:
        group = []
        nums = str(num)[::-1]
        n = len(nums)
        for i in range(0,n,3):
            group.append(nums[i:i+3][::-1])
            
        power = ["Hundred","Thousand","Million","Billion"]  
        count = ["Zero","One","Two","Three","Four",
                     "Five","Six","Seven","Eight","Nine","Ten","Eleven",
                     "Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
                     "Seventeen","Eighteen","Nineteen","Twenty"]
        twodigit = ["",  "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty","Seventy", "Eighty", "Ninety"];   
        
        
        def helperTwoDigit(curr):
            res = []
            if curr[0] == '1':
                    res.append(count[int(curr)])
            else:
                if curr[0] != '0':
                    res.append(twodigit[int(curr[0])])
                if curr[1] != '0':
                    res.append(count[int(curr[1])])
            return res

        def helperThreeDigit(curr):
            res = []
            if curr[0] != '0':
                res.append(count[int(curr[0])])
                res.append('Hundred')
                res.extend(helperTwoDigit(curr[1:]))
                # print(curr[1:])
            else:
                res.extend(helperTwoDigit(curr[1:]))
            return res

        currPower = 0
        
        if num  < 11:
            return count[num]
        elif num < 100:
            curr = []
            i = nums[::-1]
            if i[0] == '1':
                curr.append(count[int(i)])
            else:
                curr.append(twodigit[int(i[0])])
                if i[1] != '0':
                    curr.append(count[int(i[1])])
            return " ".join(curr)
        
        res = []
        for i in group:
            curr = []
            if len(i) == 3:
                curr = helperThreeDigit(i)
            elif len(i) == 2:
                curr = helperTwoDigit(i)
            else:
                if i[0] != '0':
                    curr.append(count[int(i[0])])
            if currPower != 0 and len(curr) != 0:
                curr.append(power[currPower])
            currPower+=1
            if curr:
                res.append(" ".join(curr))
        return " ".join(res[::-1])