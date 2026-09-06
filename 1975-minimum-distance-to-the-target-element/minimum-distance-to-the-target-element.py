class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min = 10001
        target_pos = []
        for i in range(len(nums)):
            if nums[i] == target:
                target_pos.append(i)
        for pos in target_pos:
            if pos <= start and min > start-pos:
                min = start-pos
            elif pos >= start and min > pos-start:
                min = pos - start
        return min