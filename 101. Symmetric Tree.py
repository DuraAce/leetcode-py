class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.isMirror(root.left, root.right)
    
    
    def isMirror(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if l is None or r is None:
            return l is r
        return l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)
