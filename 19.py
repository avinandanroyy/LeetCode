from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
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

    head = build_list([1,2,3,4,5])
    head = sol.removeNthFromEnd(head, 2)
    print_list(head)   # Output: [1, 2, 3, 5]

    nums = build_list([1])
    nums = sol.removeNthFromEnd(head,1)
    print_list(nums)   # Output: [] Wrong Answer : [1, 2, 3]

    arr = build_list([1,2])
    arr = sol.removeNthFromEnd(arr,1)
    print_list(arr)    # Output: [1]
    
