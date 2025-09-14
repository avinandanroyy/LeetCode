from typing import List, Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        li = []
        while current:
            li.append(current.val)
            current = current.next
        li.sort()
        current = head
        for val in li:
            current.val = val
            current = current.next
        return head
    
#No Output Code Is Written.