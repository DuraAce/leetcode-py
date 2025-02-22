class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        if k <= 1:
            return 0
        p = 1
        l = 0
        for r, x in enumerate(nums):
            p *= x
            while p >= k:
                p /= nums[l]
                l += 1
            ans += r - l + 1
        return ans
