from typing import Optional
class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

#Thi solution will not return anything.

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        head2 = prev

        head1 = head
        while head2:
            next1 = head1.next
            next2 = head2.next
            
            head1.next = head2
            head2.next = next1
            
            head1 = next1
            head2 = next2