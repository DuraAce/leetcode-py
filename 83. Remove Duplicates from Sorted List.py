# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        while cur and cur.next:
            nxt = cur.next
            nxt2 = nxt.next
            if cur.val == nxt.val:
                cur.next = nxt2
            else:
                cur = nxt
        return head
