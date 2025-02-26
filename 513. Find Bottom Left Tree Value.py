# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None: return None
        q = deque([root])
        ans = None
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                print(cur.val)
                if i == 0: ans = cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return ans
