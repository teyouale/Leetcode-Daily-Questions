class Solution:
    def numberOfSteps(self, num: int) -> int:
        # return len(bin(num).replace('0b',''))
        count = 0
        while num != 0:
            count+=1
            if num %2 == 0:
                num = num>>1
            else:
                num = num ^ 1
        return count
            