class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse = True)
        print(arr)
        n = len(arr)
        if n < 3:
            return 0
        ans = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                if arr[l] + arr[r] > arr[i]:
                    ans += r- l
                    l += 1
                else: 
                    r -= 1
        return ans
