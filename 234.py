from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge cases: empty or single-node lists are palindromes.
        if not head or not head.next:
            return True

        # 1. Find the end of the first half.
        first_half_end = self.get_first_half_end(head)
        
        # 2. Reverse the second half.
        second_half_start = self.reverse_list(first_half_end.next)

        # 3. Compare the first half with the reversed second half.
        p1 = head
        p2 = second_half_start
        is_palindrome = True
        while is_palindrome and p2:
            if p1.val != p2.val:
                is_palindrome = False
            p1 = p1.next
            p2 = p2.next
        
        # 4. (Optional) Restore the original list.
        first_half_end.next = self.reverse_list(second_half_start)

        return is_palindrome

    def get_first_half_end(self, node: ListNode) -> ListNode:
        """Finds the last node of the first half of the list."""
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """Reverses a linked list and returns the new head."""
        prev = None
        curr = node
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev