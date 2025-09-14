class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next

        if l1:
            tail.next = l1

        elif l2:
            tail.next = l2

        return dummy.next

#Helper Method to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    tail = dummy

    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

#Helper Method to convert linked list to list
def linkedlist_to_list(lst):
    result = []

    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]

    list1 = list_to_linkedlist(l1)
    list1 = list_to_linkedlist(l2)

    sol = Solution()

    merged = sol.mergeTwoLists(list1,list1)  
    output = linkedlist_to_list(merged)

    print(output)
