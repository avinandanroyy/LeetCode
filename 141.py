# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

def createLinkedListWithCycle(values, pos):
    if not values:
        return None
    
    nodes = []
    for val in values:
        nodes.append(ListNode(val))
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

solution = Solution()
    
head1 = createLinkedListWithCycle([3, 2, 0, -4], 1)
print(f"Test 1: {solution.hasCycle(head1)}")
    
head2 = createLinkedListWithCycle([1, 2], 0)
print(f"Test 2: {solution.hasCycle(head2)}")
    
head3 = createLinkedListWithCycle([1], -1)
print(f"Test 3: {solution.hasCycle(head3)}")
    
head4 = None
print(f"Test 4: {solution.hasCycle(head4)}")
    
head5 = createLinkedListWithCycle([1], -1)
print(f"Test 5: {solution.hasCycle(head5)}")
