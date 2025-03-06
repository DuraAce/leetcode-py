class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i, x in enumerate(nums):
            dp[i+2] = max(dp[i+1], dp[i] + nums[i])
        return dp[n+1]



# DFS solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i < 0:
                return 0
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return res
        n = len(nums)
        ans = dfs(n - 1)
        return ans
