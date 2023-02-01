class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        combined = sorted(zip(growTime,plantTime))[::-1]
        days = 0
        left = 0  
        for g,p in combined:
            left +=p
            days = max(days,g+left)
        return days  
