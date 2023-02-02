class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        one, zero, one_zero, zero_one = 0, 0, 0, 0 
        for curr in s:
            if curr == '1':
                one+=1
                zero_one+=zero
                ways+=one_zero
            else:
                zero+=1
                one_zero+=one
                ways+=zero_one
        return ways