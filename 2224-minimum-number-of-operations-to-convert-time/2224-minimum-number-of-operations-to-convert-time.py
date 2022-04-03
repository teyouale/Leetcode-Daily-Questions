class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:return 0
        x = int(current[0:2]) * 60 + int(current[3:])
        y = int(correct[0:2]) * 60 + int(correct[3:])
        x = y - x
        count = 0
        for i in [60,15,5,1]:
            count += x//i
            x = x % i
        return count