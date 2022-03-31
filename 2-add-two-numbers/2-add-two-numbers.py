# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            
            
        """
        num1 =[]
        num2 = []
        
        while l1.next != None:
            num1.append(l1.val)
            l1 = l1.next
            
        num1.append(l1.val)
        
        while l2.next != None:
            num2.append(l2.val)
            l2 = l2.next
            
        num2.append(l2.val)
        sum1_ = int(''.join(str(i) for i in reversed(num1)))
        sum2_ = int(''.join(str(i) for i in reversed(num2)))
        # temp = sum(sum1_,sum2_)
        # print(sum1_ + sum2_)        
        
        cur = dum = ListNode(0)
        
        temp = str(sum1_ + sum2_)
        # for i in 
        # print([temp.split(" "))
        
        
        temp2 = []
        for i in temp:
            # print(i)
            temp2.append(i)
            
        for i in reversed(temp2):
            cur.next = ListNode(i)
            cur = cur.next
    
        return dum.next