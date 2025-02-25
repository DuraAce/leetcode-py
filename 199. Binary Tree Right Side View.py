class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.fillAns(root, 1, ans)
        return ans

    def fillAns(self, root: Optional[TreeNode], height: int, ans: List[int]):
        if root is None:
            return
        if len(ans) < height:
            ans.append(root.val)
        height += 1
        self.fillAns(root.right, height, ans)
        self.fillAns(root.left, height, ans)
