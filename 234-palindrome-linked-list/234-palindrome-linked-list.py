# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast= head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        while slow:
            next_ = slow.next
            slow.next = pre
            pre = slow
            slow = next_
        while pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True
            