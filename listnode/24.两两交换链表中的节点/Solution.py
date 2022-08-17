# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dump_head = ListNode(next=head)
        cur = dump_head
        while cur:
            next = cur.next
            if next==None:
                return dump_head.next
            next_next = next.next
            if next_next==None:
                return dump_head.next
            next.next = next_next.next
            next_next.next = next
            cur.next = next_next
            cur = next