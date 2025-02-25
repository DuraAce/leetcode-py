### 前序遍历

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lb = -inf, rb = inf) -> bool:
        if root is None:
            return True
        x = root.val
        return lb < x < rb and self.isValidBST(root.left, lb, x) and self.isValidBST(root.right, x, rb)
