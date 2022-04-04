# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        fast = head
        while fast:
            if n == k-1: l = fast
            fast = fast.next
            n += 1
        
        slow = head
        for m in range(n-k):
            slow = slow.next
                
        l.val, slow.val = slow.val, l.val
        return head
            