from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        next_node = head.next
        head.next = self.swapPairs(next_node.next)
        next_node.next = head
        return next_node
    
# Helper to build list
def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

# Helper to print list
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == "__main__":
    sol = Solution()
    head = build_list([1, 2, 3, 4])
    new_head = sol.swapPairs(head)
    print_list(new_head)   # Output: [2, 1, 4, 3]
