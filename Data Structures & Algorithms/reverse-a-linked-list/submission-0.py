# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,temp=head,None

        while curr:
            temp2=curr.next
            curr.next=temp
            temp=curr
            curr=temp2
        return temp

         