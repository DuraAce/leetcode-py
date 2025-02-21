class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        print(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] >= target:
                    break
                else:
                    ans += 1
                    print(f'{nums[i]} {nums[j]}')
        return ans
