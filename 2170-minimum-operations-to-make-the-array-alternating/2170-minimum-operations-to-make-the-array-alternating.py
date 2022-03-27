from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
             even 3 3 4   2   3-2 4-1
             odd 1 2 3      1-1 2-1 3-1

             even 3 3 3
             odd  1 1 1

             odd 1 2 2   2-2 1-1
             even 2 2 2  2-3
        """
        if len(nums)==1:
            return 0
        
        evenC = Counter()
        oddC= Counter()

        for k,v in enumerate(nums):
            if k % 2 == 0:
                if v in evenC: evenC[v] += 1
                else:evenC[v] = 1
            else:
                if v in oddC: oddC[v] += 1
                else:oddC[v] = 1
        # print(evenC.most_common(2),oddC.most_common(2))
        
        if len(oddC.most_common(2)) < 2:
            oddC[-1]=0
        if len(evenC.most_common(2)) < 2:
            evenC[-1]=0
            
            
        # print(evenC.most_common(2),oddC.most_common(2))

        firstEven,secondEven = evenC.most_common(2)
        firstOdd,secondOdd = oddC.most_common(2)
        
        if firstEven[0] != firstOdd[0]:
            return len(nums)-(firstEven[1]+firstOdd[1])
        else:
            return len(nums) - max(firstOdd[1] + secondEven[1], firstEven[1] + secondOdd[1])