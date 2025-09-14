class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev

def createLinkedList(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


solution = Solution()

head1 = createLinkedList([1, 2, 3, 4, 5])
reversed1 = solution.reverseList(head1)
print(f"Input: [1,2,3,4,5] -> Output: {printLinkedList(reversed1)}")
    
head2 = createLinkedList([1, 2])
reversed2 = solution.reverseList(head2)
print(f"Input: [1,2] -> Output: {printLinkedList(reversed2)}")
    
head3 = createLinkedList([])
reversed3 = solution.reverseList(head3)
print(f"Input: [] -> Output: {printLinkedList(reversed3)}")
    
head4 = createLinkedList([1])
reversed4 = solution.reverseList(head4)
print(f"Input: [1] -> Output: {printLinkedList(reversed4)}")
