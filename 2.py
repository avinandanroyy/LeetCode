from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        ptr = result
        carry = 0
        
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            sum = sum % 10
            ptr.next = ListNode(sum)
            ptr = ptr.next
        
        if carry == 1:
            ptr.next = ListNode(1)
        
        return result.next

# Helper function to create a linked list from a list of digits
def create_linked_list(digits):
    head = ListNode(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = ListNode(digit)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end = " " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    l1 = create_linked_list([2, 4, 3])  # represents number 342
    l2 = create_linked_list([5, 6, 4])  # represents number 465

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Should print: 7 -> 0 -> 8