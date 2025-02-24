class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 
        cur = head
        while cur:
            n += 1
            cur = cur.next

        mid = n // 2 
        # 0 1 2 3 n = 4, mid = 2
        # 0 1 2 3 4 n = 5, mid = 2
        res = head
        for _ in range(mid):
            res = res.next

        return res


# slow and fast pointer
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
