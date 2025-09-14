# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        res=[]
        while temp:
            res.append(temp.val)
            temp=temp.next
        res.sort()    
        new_node=ListNode(res[0])    
        head=new_node
        temp=head
        prev=temp
        for i in range(1,len(res)):
            new_node=ListNode(res[i])
            prev.next=new_node
            prev=new_node
        return head    
    
#No Output Code IS Written.