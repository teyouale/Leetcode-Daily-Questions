class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted={}
        
        for k,i in enumerate(nums):
            if target - i in visted:
                return [visted[target-i],k]
            visted[i] = k
        