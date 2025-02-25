### Method 1: check if both left and right is balanced, then check if h of left and h of right is within 1 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
            
        
    def getHeight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        return max(l, r) + 1


### Method 2: define height = -1 when not balanced
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return False if self.getHeight(root) == -1 else True
    
    def getHeight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        else:
            return max(l, r) + 1
