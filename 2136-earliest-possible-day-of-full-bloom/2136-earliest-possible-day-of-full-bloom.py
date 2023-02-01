class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        combined = sorted(zip(growTime,plantTime))
        days = combined[0][1] + combined[0][0] 
        for g,p in combined[1:]:
            days = max(days, g) + p
        return days 