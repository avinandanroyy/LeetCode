class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next

head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete = head.next

sol = Solution()
sol.deleteNode(node_to_delete)

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
