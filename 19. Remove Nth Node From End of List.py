# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        
        # 1 2 3 4 5
        # n = 2, cnt = 5
        pre = dummy
        for _ in range(cnt - n):
            pre = pre.next
        pre.next = pre.next.next

        return dummy.next
        






        
