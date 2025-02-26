class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = deque([root])
        order = 1

        while q:
            n = len(q)
            lvl = []
            for _ in range(n):
                cur = q.popleft()
                lvl.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if order == -1: lvl.reverse()
            result.append(lvl)
            order *= -1
            
        return result        
