class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return [-1, -1]
        start = lower_bound(nums, target)
        print(start)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1)
        return [start, end - 1]

def lower_bound(nums: List[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l
