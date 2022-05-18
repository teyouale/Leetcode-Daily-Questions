class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(map(str,digits))
        
        return  [int(i) for i in str(int(num)+1)]