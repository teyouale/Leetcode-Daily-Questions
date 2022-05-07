class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_max = -math.inf
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < second_max:
                return True
            
            while stack and nums[i] > stack[-1]:
                ele = stack.pop()
                second_max = max(second_max,ele)
            
            stack.append(nums[i])
            
        return False