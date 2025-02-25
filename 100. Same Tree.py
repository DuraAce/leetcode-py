class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        return p.val == q.val and l and r
