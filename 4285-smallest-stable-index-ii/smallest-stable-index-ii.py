class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] - nums[-1] > k:
            return -1
        for i in range(0,n):
            if max(nums[0:i+1]) - min(nums[i:n]) <= k:
                return i
        return -1
        