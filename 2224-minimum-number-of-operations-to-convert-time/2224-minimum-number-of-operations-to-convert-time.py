class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:return 0
        x = current.split(':')
        y = correct.split(':')
        hourDiff = int(y[0])-int(x[0])
        mintDiff = int(y[1])-int(x[1])
        x = hourDiff*60 + mintDiff
        count = 0
        while x!=0:
            if x-60 >= 0:
                x-=60
            elif x-15>=0:
                x-=15
            elif x-5>=0:
                x-=5
            else:
                x-=1
            count+=1
        return count