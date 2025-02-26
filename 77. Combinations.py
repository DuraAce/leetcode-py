class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(i):
            if i < 1:
                return

            path.append(i)
            if len(path) == k:
                ans.append(path.copy())
                return

            for l in range(i - 1, 0, -1):
                # print(f"i: {i}, l:{l}")
                dfs(l)
                path.pop()
            
        # n = 4, k = 2
        for j in range(n, k - 1, -1):
            path = []
            dfs(j)
        return ans
